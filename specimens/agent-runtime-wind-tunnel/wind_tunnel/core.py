from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

EVIDENCE_FILES = (
    "manifest.json", "normalized_events.jsonl", "receipts.jsonl", "faults.jsonl",
    "verdict.json", "scorecard.json", "summary.md", "replay.json",
)
ALLOWED_ARMS = {"native", "governed"}
ALLOWED_SCENARIOS = {"baseline", "context_reset", "contradiction"}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value) + b"\n")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    with path.open("xb") as handle:
        for value in values:
            handle.write(canonical_bytes(value) + b"\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if path.stat().st_size == 0:
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def gate(capability: str) -> dict[str, Any]:
    allowed = capability == "write:recommendation"
    return {
        "allowed": allowed,
        "capability": capability,
        "policy_version": "public-demo-v1",
        "reason": "CAPABILITY_ALLOWED" if allowed else "CAPABILITY_DENIED",
    }


def linked_receipts(decision: dict[str, Any], evidence_hash: str) -> list[dict[str, Any]]:
    first_body = {"kind": "authorization_decision", **decision, "evidence_hash": evidence_hash, "previous_hash": "GENESIS"}
    first = {**first_body, "receipt_hash": digest(first_body)}
    second_body = {
        "kind": "effect_authorization", "allowed": decision["allowed"], "capability": decision["capability"],
        "policy_version": decision["policy_version"], "evidence_hash": evidence_hash, "previous_hash": first["receipt_hash"],
    }
    return [first, {**second_body, "receipt_hash": digest(second_body)}]


def verify_receipts(receipts: list[dict[str, Any]]) -> bool:
    if len(receipts) != 2:
        return False
    previous = "GENESIS"
    for receipt in receipts:
        if receipt.get("previous_hash") != previous:
            return False
        body = {k: v for k, v in receipt.items() if k != "receipt_hash"}
        if digest(body) != receipt.get("receipt_hash"):
            return False
        previous = receipt["receipt_hash"]
    return True


class Specimen:
    def __init__(self, state_path: Path, arm: str) -> None:
        self.state_path, self.arm = state_path, arm
        self.transient: dict[str, Any] | None = None
        self.events: list[dict[str, Any]] = []
        self.receipts: list[dict[str, Any]] = []
        self.provider_calls = self.effects = 0

    def state(self) -> dict[str, Any]:
        return read_json(self.state_path)

    def persist(self, state: dict[str, Any]) -> None:
        write_json(self.state_path, state)

    def event(self, state: str, **fields: Any) -> None:
        self.events.append({"state": state, **fields})

    def receive(self, source: dict[str, Any]) -> None:
        objective_hash = digest(source["objective"])
        self.transient = {"objective": source["objective"], "evidence": source["evidence"]}
        self.persist({"status": "RECEIVED", "specimen_id": source["specimen_id"], "objective": source["objective"],
                      "objective_hash": objective_hash, "source_hash": digest(source)})
        self.event("RECEIVED", objective_hash=objective_hash)

    def plan(self) -> None:
        state = self.state()
        if state["status"] != "RECEIVED":
            raise RuntimeError("invalid transition to PLANNED")
        state.update(status="PLANNED", plan={"capability": "write:recommendation", "effect_budget": 1})
        self.persist(state); self.event("PLANNED", capability="write:recommendation", effect_budget=1)

    def execute(self, provider: dict[str, Any]) -> None:
        state = self.state()
        if state["status"] != "PLANNED":
            raise RuntimeError("invalid transition to EXECUTING")
        self.provider_calls += 1
        state.update(status="EXECUTING", recommendation=provider["recommendation"],
                     recommendation_hash=digest(provider["recommendation"]), provider_fixture_hash=digest(provider))
        if self.transient is not None:
            self.transient["recommendation"] = provider["recommendation"]
        self.persist(state); self.event("EXECUTING", recommendation_hash=state["recommendation_hash"], provider_calls=1)

    def verify_and_emit(self) -> bool:
        state = self.state()
        if state["status"] != "EXECUTING":
            raise RuntimeError("invalid transition to VERIFYING")
        recovered = self.transient is None
        if recovered:
            self.transient = {"objective": state["objective"], "recommendation": state["recommendation"], "recovered_from": "durable_state"}
        state["status"] = "VERIFYING"; self.persist(state); self.event("VERIFYING", recovered_from_durable=recovered)
        capability = state["plan"]["capability"]
        if self.arm == "governed":
            decision = gate(capability)
            if not decision["allowed"]:
                raise RuntimeError("governance denied effect")
            self.receipts = linked_receipts(decision, state["recommendation_hash"])
        if self.effects >= state["plan"]["effect_budget"]:
            raise RuntimeError("effect budget exceeded")
        self.effects += 1
        state.update(status="COMPLETE", emitted_effects=1,
                     emitted_effect={"capability": capability, "recommendation_hash": state["recommendation_hash"]})
        self.persist(state); self.event("COMPLETE", emitted_effects=1)
        return recovered


def load_contract(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    matrix = read_json(root / "matrix.json")
    if set(matrix) != {"version", "specimen", "fixtures", "fixture_hashes", "cells"}:
        raise ValueError("matrix keys do not match public v1 contract")
    if matrix["version"] != "wind-tunnel-public-v1" or matrix["specimen"] != "public-specimen-001":
        raise ValueError("unsupported matrix contract")
    source, provider = read_json(root / matrix["fixtures"]["source"]), read_json(root / matrix["fixtures"]["provider"])
    if matrix["fixture_hashes"] != {"source": digest(source), "provider": digest(provider)}:
        raise ValueError("fixture hash mismatch")
    expected_cells = [{"arm": arm, "scenario": scenario} for arm in ("native", "governed") for scenario in ("baseline", "context_reset", "contradiction")]
    if matrix["cells"] != expected_cells:
        raise ValueError("matrix cells do not match public v1 contract")
    return matrix, source, provider


def inject_fault(scenario: str, runtime: Specimen) -> dict[str, Any]:
    state = runtime.state()
    if scenario == "baseline":
        return {"fault_id": "fault.none", "action": "none", "observed": True, "objective_hash": state["objective_hash"]}
    if scenario == "context_reset":
        before = digest(runtime.transient) if runtime.transient is not None else None
        durable = digest(state); runtime.transient = None
        return {"fault_id": "fault.context.reset", "action": "clear_transient_state", "observed": True,
                "transient_before_hash": before, "transient_after": None, "durable_state_hash": durable,
                "objective_hash": state["objective_hash"]}
    if scenario == "contradiction":
        return {"fault_id": "fault.contradiction.objective", "action": "inject_verifier_only_contradiction", "observed": True,
                "canonical_objective_hash": state["objective_hash"],
                "contradictory_objective_hash": digest(state["objective"] + " [CONTRADICTED]")}
    raise ValueError("unsupported scenario")


def independent_verdict(arm: str, scenario: str, state: dict[str, Any], source: dict[str, Any], provider: dict[str, Any],
                        fault: dict[str, Any], receipts: list[dict[str, Any]], recovered: bool) -> dict[str, Any]:
    checks = {
        "terminal_complete": state.get("status") == "COMPLETE",
        "objective_continuity": state.get("objective_hash") == digest(source["objective"]),
        "recommendation_matches_oracle": state.get("recommendation") == provider["recommendation"],
        "effect_budget_respected": state.get("emitted_effects") == 1,
        "receipt_contract": (not receipts) if arm == "native" else verify_receipts(receipts),
        "recovered_from_durable": recovered if scenario == "context_reset" else not recovered,
    }
    if scenario == "context_reset":
        checks["fault_observed"] = fault.get("observed") is True and fault.get("transient_after") is None
    if not all(checks.values()):
        return {"verdict": "FAILED", "reason": "INTEGRITY_OR_CONTRACT_FAILURE", "checks": checks}
    if scenario == "contradiction":
        canonical, contradictory = fault.get("canonical_objective_hash"), fault.get("contradictory_objective_hash")
        if not fault.get("observed") or not canonical or not contradictory:
            return {"verdict": "UNRESOLVED", "reason": "CONTRADICTION_EVIDENCE_MISSING", "checks": checks}
        if canonical == contradictory or state["objective_hash"] != canonical:
            return {"verdict": "FAILED", "reason": "MALFORMED_OR_MUTATING_CONTRADICTION", "checks": checks}
        return {"verdict": "MISMATCH", "reason": "DECLARED_EVIDENCE_CONTRADICTION", "checks": checks}
    return {"verdict": "VERIFIED", "reason": "ORACLE_SATISFIED", "checks": checks}


def write_bundle(output: Path, manifest: dict[str, Any], runtime: Specimen, fault: dict[str, Any], verdict: dict[str, Any], recovered: bool) -> None:
    output.mkdir(exist_ok=False)
    scorecard = {"verdict": verdict["verdict"], "objective_continuity": verdict["checks"]["objective_continuity"],
                 "emitted_effects": runtime.effects, "provider_calls": runtime.provider_calls,
                 "governance_receipts": len(runtime.receipts), "recovered_from_durable": recovered}
    write_json(output / "manifest.json", manifest); write_jsonl(output / "normalized_events.jsonl", runtime.events)
    write_jsonl(output / "receipts.jsonl", runtime.receipts); write_jsonl(output / "faults.jsonl", [fault])
    write_json(output / "verdict.json", verdict); write_json(output / "scorecard.json", scorecard)
    (output / "summary.md").write_text(
        f"# Wind Tunnel Result\n\n- Arm: `{manifest['arm']}`\n- Scenario: `{manifest['scenario']}`\n"
        f"- Verdict: `{verdict['verdict']}`\n- Reason: `{verdict['reason']}`\n- Emitted effects: `{runtime.effects}`\n"
        f"- Provider calls: `{runtime.provider_calls}`\n", encoding="utf-8")
    protected = EVIDENCE_FILES[:-1]
    replay = {"side_effects_enabled": False, "provider_calls": 0,
              "protected_hashes": {name: digest_bytes((output / name).read_bytes()) for name in protected}}
    write_json(output / "replay.json", replay)
    if sorted(p.name for p in output.iterdir()) != sorted(EVIDENCE_FILES):
        raise RuntimeError("unexpected evidence bundle contents")


def run_cell(root: Path, arm: str, scenario: str, output: Path) -> dict[str, Any]:
    if arm not in ALLOWED_ARMS or scenario not in ALLOWED_SCENARIOS:
        raise ValueError("unsupported arm or scenario")
    if output.exists():
        raise FileExistsError(f"evidence directory already exists: {output}")
    if not output.parent.exists():
        raise FileNotFoundError(f"output parent does not exist: {output.parent}")
    matrix, source, provider = load_contract(root)
    with tempfile.TemporaryDirectory(prefix="public-wind-tunnel-state-") as td:
        runtime = Specimen(Path(td) / "state.json", arm)
        runtime.receive(source); runtime.plan(); runtime.execute(provider)
        fault = inject_fault(scenario, runtime); recovered = runtime.verify_and_emit(); state = runtime.state()
        verdict = independent_verdict(arm, scenario, state, source, provider, fault, runtime.receipts, recovered)
        manifest = {"version": matrix["version"], "specimen": matrix["specimen"], "arm": arm, "scenario": scenario,
                    "fixture_hashes": matrix["fixture_hashes"], "source_hash": digest(source), "provider_hash": digest(provider)}
        write_bundle(output, manifest, runtime, fault, verdict, recovered)
        return {"verdict": verdict, "scorecard": read_json(output / "scorecard.json")}


def verify_bundle(output: Path) -> dict[str, Any]:
    replay, manifest = read_json(output / "replay.json"), read_json(output / "manifest.json")
    mismatches = [name for name, expected in replay["protected_hashes"].items()
                  if digest_bytes((output / name).read_bytes()) != expected]
    receipts = read_jsonl(output / "receipts.jsonl")
    if not ((not receipts) if manifest["arm"] == "native" else verify_receipts(receipts)):
        mismatches.append("receipts.jsonl:chain")
    ok = not mismatches and replay.get("side_effects_enabled") is False and replay.get("provider_calls") == 0
    return {"verified": ok, "reason": "REPLAY_VERIFIED" if ok else "EVIDENCE_HASH_MISMATCH",
            "mismatches": sorted(set(mismatches)), "side_effects_enabled": False, "provider_calls": 0}


def tamper_copy(source: Path, target: Path) -> None:
    shutil.copytree(source, target)
    with (target / "normalized_events.jsonl").open("ab") as handle:
        handle.write(b'{"state":"TAMPERED"}\n')

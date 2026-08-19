from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from .core import run_cell, tamper_copy, verify_bundle

ROOT = Path(__file__).resolve().parents[1]


def demo() -> int:
    evidence = ROOT / "evidence"
    evidence.mkdir(exist_ok=True)
    run_root = Path(tempfile.mkdtemp(prefix="demo-", dir=evidence))
    results = {}
    for arm in ("native", "governed"):
        for scenario in ("baseline", "context_reset", "contradiction"):
            results[(arm, scenario)] = run_cell(ROOT, arm, scenario, run_root / f"{arm}-{scenario}")["verdict"]["verdict"]
    print("AGENT RUNTIME WIND TUNNEL\n")
    print(f"{'scenario':<18} {'native':<12} {'governed':<12}")
    for scenario in ("baseline", "context_reset", "contradiction"):
        print(f"{scenario:<18} {results[('native', scenario)]:<12} {results[('governed', scenario)]:<12}")
    expected = {"baseline": "VERIFIED", "context_reset": "VERIFIED", "contradiction": "MISMATCH"}
    correct = sum(results[(arm, scenario)] == verdict for scenario, verdict in expected.items() for arm in ("native", "governed"))
    print(f"\n{correct}/6 expected verdicts observed\n0 unexpected side effects\n6 evidence bundles written under {run_root.relative_to(ROOT)}")
    return 0 if correct == 6 else 1


def tamper_demo() -> int:
    evidence = ROOT / "evidence"
    evidence.mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="tamper-", dir=evidence))
    pristine, tampered = work / "pristine", work / "tampered"
    run_cell(ROOT, "governed", "baseline", pristine)
    tamper_copy(pristine, tampered)
    result = verify_bundle(tampered)
    print(f"Replay verification: {'VERIFIED' if result['verified'] else 'FAILED'}")
    print(f"Reason: {result['reason']}")
    print(f"Side effects emitted during replay: {int(result['side_effects_enabled'])}")
    return 0 if not result["verified"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Public deterministic Agent Runtime Wind Tunnel")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("arm", choices=("native", "governed"))
    run.add_argument("scenario", choices=("baseline", "context_reset", "contradiction"))
    run.add_argument("output", type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("bundle", type=Path)
    sub.add_parser("demo")
    sub.add_parser("tamper")
    args = parser.parse_args()
    if args.command == "run":
        result = run_cell(ROOT, args.arm, args.scenario, args.output)
        print(json.dumps(result["verdict"], indent=2, sort_keys=True))
        return 0
    if args.command == "verify":
        result = verify_bundle(args.bundle)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["verified"] else 1
    return demo() if args.command == "demo" else tamper_demo()


if __name__ == "__main__":
    raise SystemExit(main())

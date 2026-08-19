# Deployment 03 — Runtime Wind Tunnel

## System Problem

Agent runtimes are easy to demo and hard to compare.

A claim like "this governance layer makes the agent more reliable" is weak if the experiment changes the model, prompt, workflow, retry policy, verifier, and evidence format at the same time.

The problem was to create an evaluation surface where runtime behavior could be pressured without letting the measurement harness manufacture the answer.

The initial question became:

> Can the same deterministic specimen be run through native and governed boundaries under the same workload and fault schedule, while preserving specimen ownership of its own workflow and acceptance semantics?

---

## Public Proof — Run It

The private Runtime Lab implementation is not required to evaluate the core engineering claim.

A deliberately small public specimen lives at [`specimens/agent-runtime-wind-tunnel/`](../specimens/agent-runtime-wind-tunnel/). It has no API keys, network calls, Docker requirement, or live LLM dependency.

From the portfolio root:

```bash
cd specimens/agent-runtime-wind-tunnel
make test
make demo
make tamper
```

The public specimen was validated before publication with **14/14 tests passing**. Its six predeclared cells produce:

```text
scenario           native       governed
baseline           VERIFIED     VERIFIED
context_reset      VERIFIED     VERIFIED
contradiction      MISMATCH     MISMATCH
```

`make tamper` intentionally corrupts recorded evidence and requires verification-only replay to fail with `EVIDENCE_HASH_MISMATCH` while emitting zero replay side effects.

The public specimen is intentionally not a copy of Runtime Lab. It extracts the proof primitive: fixed workload, declared faults, native/governed comparison, deterministic authority boundary, independent verdicts, exact evidence bundles, replay, and tamper detection.

One useful difference is deliberate: because the synthetic public runtime is fully controlled, its `context_reset` scenario destroys real transient runtime state and reconstructs verification state from durable storage. The current private Runtime Lab first slice remains narrower and only clears adapter-owned observation state.

---

## Scope

Runtime Lab is **Specimen 001**.

The first Wind Tunnel slice is intentionally narrow:

- local only;
- deterministic fixtures only;
- one specimen;
- one workload;
- two experiment arms;
- three scenarios;
- no live provider calls;
- no publishing or production side effects;
- no aggregate score without a declared weighting contract.

This is an experiment harness, not a model-quality benchmark and not a deployment claim.

---

## Separation of Ownership

The experiment is useful only if ownership boundaries stay explicit.

### Runtime Lab owns

- the ten-step workflow;
- native state transitions;
- artifact/event laws;
- provider registry;
- the exclusive authority to produce its native `ACCEPTED` state.

### CEINIT owns

- experiment control;
- specimen adaptation;
- normalization;
- fault scheduling;
- independent verification;
- scoring.

### Veynit owns only the governed boundary

- external authorization decisions;
- linked hash-chained receipts;
- verification-only replay behavior.

The governing invariant is:

> Provider completion does not imply acceptance.

The experiment harness is not allowed to overwrite specimen truth just because an external model or wrapper reports success.

---

## Experiment Matrix

The first complete matrix is:

| Dimension | Values |
|---|---|
| Specimen | `specimen-001` |
| Arms | `native`, `veynit_governed` |
| Scenarios | `baseline`, `context_reset`, `contradiction_injection` |
| Workload | fixed `research_to_social_v1` success workload |
| Provider | immutable deterministic mock fixture |
| Repetitions | one per arm/scenario |

That produces six deterministic runs.

Only the arm, scenario, and scenario-bound fault schedule are allowed to vary. Workload, objective, initial status, provider fixture, source fixture, oracle, and declared hashes stay fixed across arms.

This prevents the harness from "improving" one side by quietly giving it a different task.

---

## Faults

### Baseline

No disturbance. The harness still records the declared no-fault boundary so absence of a fault is explicit rather than inferred.

### Context reset

The first private Runtime Lab slice clears only an **adapter-owned lifecycle observation cache** after a committed workflow boundary.

This is deliberately constrained. Runtime Lab does not expose a safe resumable mid-stack memory-reset primitive, so the private harness does not pretend it is testing one.

The public synthetic specimen goes one step further: it owns a real transient runtime context, destroys it after `EXECUTING`, and requires the next stage to recover from durable state.

### Contradiction injection

The harness creates a deterministic objective-hash contradiction for the **independent verifier** without mutating specimen state, fixture bytes, normalized events, the adapter cache, or the continuity anchor.

The expected external result is:

```text
MISMATCH / DECLARED_EVIDENCE_CONTRADICTION
```

If required contradiction evidence is missing, the correct result is `UNRESOLVED`, not an invented pass/fail.

Malformed or tampered evidence is `FAILED` rather than being downgraded into a clean experiment result.

---

## Evidence Bundle

Every successful invocation writes exactly eight append-once artifacts:

1. `manifest.json` — validated experiment identity and oracle;
2. `normalized_events.jsonl` — ordered semantic specimen events with volatile fields removed;
3. `receipts.jsonl` — empty for native, linked external receipts for governed;
4. `faults.jsonl` — scheduled/observed fault evidence;
5. `verdict.json` — independent terminal verdict and cited evidence;
6. `scorecard.json` — evidence-backed metrics and deterministic counts;
7. `summary.md` — concise human-readable outcome;
8. `replay.json` — verification-only replay result.

Outputs use create-exclusive semantics so an existing evidence directory cannot be silently overwritten.

Fixtures are hash-checked before the run. The private harness additionally executes from bounded immutable snapshots.

---

## Independent Verdicts

The external verifier does not call the provider and does not treat specimen self-report as proof.

| Verdict | Meaning |
|---|---|
| `VERIFIED` | required evidence supports the declared property |
| `MISMATCH` | well-formed evidence contradicts the oracle/continuity requirement |
| `UNRESOLVED` | required evidence is absent |
| `FAILED` | evidence is malformed, duplicated, tampered, or invalid |

This vocabulary is important because "we cannot determine the result" is different from "the system failed the test."

---

## Replay Boundary

Replay is verification only.

It records:

```text
side_effects_enabled = false
provider_calls = 0
```

Replay cannot invoke the specimen runtime, a publisher, or any external system in the public specimen. Its purpose is to validate already-recorded evidence and receipt linkage without re-emitting effects.

---

## Current Maturity

The private Runtime Lab feature branch documents the Wind Tunnel as:

- **implemented**;
- **tested**;
- **fixture-only**;
- **not deployed**.

The public specimen is:

- **implemented**;
- **tested (14-test dependency-free suite)**;
- **publicly runnable**;
- **not a production runtime**;
- **not a model benchmark**.

Neither surface claims:

- live-provider comparison;
- statistical generalization;
- production Veynit policy service behavior;
- distributed execution;
- publication or external production side effects.

Those exclusions are part of the experiment contract, not missing marketing copy.

---

## Why This Matters for Forward-Deployed Work

Forward-deployed engineers often have to answer questions like:

- Did the new agent/runtime actually improve the workflow?
- Did the governance layer improve safety without changing the task?
- Did a failure recover because of the system, or because the retry hid it?
- Can we reproduce the result?
- Can an independent verifier inspect the evidence without trusting the component under test?

The Wind Tunnel turns those questions into an explicit experiment contract.

It is also an example of the feedback loop from field engineering into platform capability:

```text
production agent failures
  -> need for stronger runtime claims
  -> controlled specimen harness
  -> explicit fault / verifier / evidence boundaries
  -> reusable runtime evaluation capability
```

---

## Forward-Deployed Takeaway

The important product insight is not "benchmark more models." It is:

> When customers depend on agentic systems, the platform needs a way to distinguish model output, runtime behavior, authorization, emitted effects, and verifier acceptance under controlled pressure.

That is the role of the Wind Tunnel.

[Run the public specimen](../specimens/agent-runtime-wind-tunnel/) · [Back to portfolio](../README.md) · [Previous: Governed Agent Execution](02-governed-agent-execution.md)

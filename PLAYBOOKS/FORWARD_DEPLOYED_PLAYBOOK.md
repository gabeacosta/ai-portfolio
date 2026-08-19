# Forward Deployed Engineering Playbook

## Purpose

This is the operating playbook I use when a customer problem is too cross-functional for a clean product ticket and too consequential for a disconnected proof of concept.

The goal is to move from ambiguity to a production-capable vertical slice while preserving enough evidence to learn what should become platform capability.

```text
Discover -> Specify -> Scope -> Build -> Integrate -> Ship -> Observe -> Evaluate -> Harden -> Extract
```

The order matters. The amount of ceremony does not. Small problems should stay small.

---

## 1. Discover

### Objective

Understand the operating system around the problem before choosing the technical solution.

### Questions

- Who performs the workflow today?
- What starts it?
- What state already exists?
- Where does it fail or leak?
- What is the business consequence of delay or error?
- Which external actions require permission?
- What service level actually matters?
- What can remain manual in v1?

### Output

A small set of measurable statements.

Bad:

> Build an AI assistant for leads.

Better:

> 100+ leads arrive each week, only ~40 receive timely contact, and hot leads should receive first contact inside 15 minutes without replacing the CRM as the source of truth.

---

## 2. Specify the Outcome

Define success independently of the implementation.

A useful specification includes:

- user/business outcome;
- in-scope workflow;
- explicit non-goals;
- authority boundaries;
- systems of record;
- failure semantics;
- measurable acceptance criteria.

If the system cannot be evaluated without asking the builder whether it "looks right," the specification is too weak.

---

## 3. Scope the Smallest Complete Slice

A forward-deployed slice should be vertically complete:

```text
input
  -> state
  -> decision
  -> action
  -> evidence
  -> recovery
```

Avoid building a model, dashboard, policy service, queue, and orchestration framework as five separate demonstrations.

Prefer one workflow that can be used end to end.

### Scope test

Before implementation, answer:

- What happens on success?
- What happens on dependency failure?
- What happens on duplicate input?
- What happens after a partial external effect?
- Who can retry?
- Who can approve?
- How is the outcome verified?

---

## 4. Map State and Authority

Two diagrams prevent a large class of failures.

### State ownership

```text
source event -> normalized object -> durable owner -> derived views
```

Every important field should have one authoritative owner.

### Authority ownership

```text
proposal -> policy decision -> approval (if required) -> effect -> evidence
```

A model proposal must not silently become authorization.

For high-consequence workflows, define:

- caller identity;
- capability;
- target scope;
- policy/version;
- budget/quota;
- approval requirement;
- evidence emitted.

---

## 5. Build the Thin Path First

The first implementation should prove the integration path before optimizing model sophistication.

Typical order:

1. deterministic input fixture;
2. state transition;
3. stubbed or deterministic decision;
4. bounded effect adapter;
5. evidence emission;
6. operator-visible outcome;
7. live provider/model integration.

This makes failures attributable. If the plumbing cannot survive deterministic input, adding model variability only makes diagnosis harder.

---

## 6. Integrate at Real Boundaries

Test the seams that production will actually exercise:

- webhook signatures;
- authentication;
- idempotency;
- rate limits;
- CRM/API consistency;
- schema drift;
- queue retries;
- timeout behavior;
- file/write scopes;
- provider fallback;
- network failure;
- partial success.

Do not let mocks erase the property being tested.

---

## 7. Ship With a Recovery Path

Before calling a deployment production-capable, define operator recovery.

Minimum questions:

- How does an operator know the workflow is stuck?
- Can they identify the last durable state?
- Can they distinguish retryable from non-retryable failure?
- Can they replay without duplicating side effects?
- Can they disable or narrow authority quickly?
- What is the rollback path?

A deployment that only works while the builder is watching it is not hardened.

---

## 8. Observe the System

Telemetry should support diagnosis; evidence should support claims.

### Telemetry

Useful for:

- latency;
- queue depth;
- errors;
- resource usage;
- request traces;
- provider outcomes.

### Evidence

Useful for proving:

- which policy allowed an action;
- which effect was emitted;
- which state transition committed;
- which fault was injected;
- which verifier produced the terminal verdict;
- whether replay emitted side effects.

The stronger the consequence of the action, the stronger the evidence requirement should be.

---

## 9. Pressure-Test the Failure Paths

Start with the failures that would produce the largest hidden consequence.

Common classes:

- dependency unavailable while health still reports green;
- duplicate delivery;
- timeout after an effect is emitted;
- retry after partial success;
- stale authority;
- provider drift;
- malformed tool result;
- context loss/restart;
- evidence contradiction;
- concurrent writes;
- state-store corruption;
- silent fallback.

For agent runtimes, provider success should never be treated as sufficient proof of workflow success.

---

## 10. Convert Incidents Into Regression Proof

When production breaks:

1. capture the observable symptom;
2. identify the real failed property;
3. reproduce it deterministically when possible;
4. add the narrowest control that fixes the property;
5. write a regression test/evidence path;
6. document what the fix does **not** prove.

Examples in this portfolio:

- lying health endpoint -> dependency-aware readiness;
- audit rotation reset -> durable prior-chain anchoring;
- ephemeral hotfix drift -> startup fingerprinting.

---

## 11. Measure Business and Technical Outcomes Separately

Both matter.

### Business

Examples:

- leads contacted;
- time to first contact;
- manual minutes removed;
- conversion throughput;
- cost per workflow;
- operator interventions.

### Technical

Examples:

- error rate;
- retry count;
- duplicate effects;
- policy denies;
- recovery success;
- continuity;
- evidence integrity;
- provider calls;
- latency.

Do not hide a weak business outcome behind strong benchmark scores, or hide an unsafe runtime behind strong revenue numbers.

---

## 12. Extract Only What Repeats

After the deployment is working, ask:

- Which logic was customer-specific?
- Which integration pattern repeated?
- Which failure mode is likely to exist elsewhere?
- Which interface stayed stable under iteration?
- What would save the next deployment meaningful time or risk?

Promote only those pieces.

```text
field-specific code
  -> repeated pattern
  -> stable contract
  -> reusable primitive
  -> platform feature
```

Examples from this portfolio:

- voice workflow pressure -> VoxMaestro orchestration primitives;
- agent action pressure -> governed MCP authorization primitives;
- runtime incidents -> readiness/fingerprint controls;
- runtime assurance pressure -> Wind Tunnel evidence/verifier boundaries.

---

## 13. Maturity Language

Use precise labels:

| Label | Required meaning |
|---|---|
| Implemented | code/configuration exists |
| Tested | automated behavior checks exist |
| Verified | evidence supports the claimed property |
| Accepted | designated gate/verifier authorized the result |
| Deployed | running in intended operating environment |

Never collapse these into "done."

---

## Engagement Exit Criteria

A successful forward-deployed engagement should leave behind:

### Customer outcome

The workflow is measurably better.

### Operational control

The important failure and recovery paths are known, bounded, and visible.

### Product feedback

The product/platform team can point to concrete primitives that deserve reuse and concrete customer-specific logic that should remain local.

### Evidence

The claims used to justify the deployment can be traced to tests, receipts, telemetry, or clearly labeled operating reports.

---

## Field Checklist

- [ ] Define the business outcome before selecting the model.
- [ ] Name the system of record for every important state transition.
- [ ] Define authority before granting tool access.
- [ ] Make the first slice vertically complete.
- [ ] Use deterministic fixtures before live-provider variability where possible.
- [ ] Define idempotency and retry behavior.
- [ ] Add operator-visible degraded states.
- [ ] Distinguish telemetry from evidence.
- [ ] Test at least one meaningful failure path before launch.
- [ ] Document rollback/recovery.
- [ ] Separate implemented/tested/verified/accepted/deployed.
- [ ] Productize only the patterns that recur.

[Back to portfolio](../README.md) · [How I Work](../HOW_I_WORK.md)

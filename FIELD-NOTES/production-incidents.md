# Field Notes — Production Incidents That Changed the Architecture

Forward-deployed systems become credible when production failures change the design.

These are three incidents where the initial architecture looked reasonable, production exposed a different property, and the fix became a reusable control rather than a one-off patch.

---

## Incident 01 — The Health Check Lied for Six Days

### Symptom

A runtime `/health` endpoint continued returning:

```json
{"status":"ok"}
```

while the database container it depended on had been recreated into a `Created` state and never actually started.

The API process was alive, so the endpoint stayed green. Database-dependent background work failed for six days.

### Failed property

The endpoint answered:

> Is this HTTP process responsive?

while operators interpreted it as:

> Is this service able to perform the work it is responsible for?

Those are different questions.

### Fix

The public reliability slice in [`clue-runtime`](https://github.com/gabeacosta/clue-runtime) separates two interfaces:

- `/health` remains HTTP 200 for process/liveness-oriented consumers but reports dependency degradation honestly in its body;
- `/health/ready` returns 503 when the dependency is unavailable so orchestration and alerting systems can act on the failure.

The tests cover both healthy and unhealthy directions. A health check tested only on the happy path would not prove it is better than an endpoint that always returns green.

### Reusable lesson

**Health is audience-specific.**

A reverse proxy, an orchestrator, and a human operator may need different semantics. The endpoint contract must state what it proves.

---

## Incident 02 — The Tamper-Evident Audit Chain Was Not One Chain

### Symptom

A governed agent system used hash-chained audit entries so each record committed to the prior record.

The implementation worked until log rotation.

When the new active file was empty, the writer initialized the next record against a sentinel instead of the last durable hash. The apparent chain silently restarted at every rotation boundary.

The public-safe repo documents that roughly 60% of records in the affected deployment were anchored to the sentinel rather than one continuous chain.

### Failed property

The system claimed:

> deleting or rewriting history will break the chain.

But if the chain legitimately restarted each day, an entire rotated segment could disappear without violating the active segment's linkage.

The issue was not "logging." It was loss of continuity across an operational lifecycle event.

### Fix

The writer now recovers the prior durable chain tail when the active file is empty.

The regression proof covers both:

- rotation with existing history must continue from the durable tail;
- a truly fresh installation with no history may start from the sentinel.

Concurrent read-tail → append behavior is also protected so simultaneous writers cannot fork the chain.

Public proof: [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine).

### Reusable lesson

**Evidence systems have lifecycle failure modes too.**

A cryptographic primitive can be correct locally while the operational system still violates the property it is meant to guarantee.

---

## Incident 03 — The Hotfix Disappeared on Container Recreation

### Symptom

A production issue was patched by copying corrected code into a running container.

The live container behaved correctly afterward.

Later, the container was recreated from its original image. The ephemeral file override disappeared and the old behavior returned without an explicit deployment error.

### Failed property

Operators assumed:

> this node is running the corrected implementation.

The infrastructure could only prove:

> this node started successfully from some image.

The running bytes of the load-bearing code path were not being identified.

### Fix

The runtime reliability slice added a startup fingerprint for the exact files defining a critical signing/verification path.

On startup, the system hashes those bytes and exposes/logs a short fingerprint. Two nodes—or the same node before and after recreation—can be compared directly.

This control is intentionally narrow:

- it does not prove the code is correct;
- it does not replace CI;
- it does not automatically block startup;
- it does reveal when supposedly equivalent deployments are running different bytes.

Public proof: [`clue-runtime`](https://github.com/gabeacosta/clue-runtime).

### Reusable lesson

**Deployment identity should be observable at the property boundary that matters.**

Version labels and container health are insufficient when the incident class is runtime/image drift.

---

## Pattern Across the Three Incidents

All three failures came from the same architectural mistake:

> a convenient proxy was treated as proof of a stronger property.

| Proxy | Assumed property | Reality |
|---|---|---|
| HTTP 200 | service is operational | process was alive, DB was unavailable |
| local hash linkage | continuous tamper-evident history | chain restarted at rotation |
| running container | corrected code is deployed | recreated image restored old bytes |

The correction pattern was also consistent:

```text
claim
  -> identify the property actually needed
  -> reproduce the gap
  -> instrument the real boundary
  -> add deterministic regression proof
```

---

## How This Changes My Forward-Deployed Work

I now pressure-test claims by asking what evidence would falsify them.

Examples:

- If a service says it is healthy, which dependency failure makes that statement false?
- If an audit log says it is tamper-evident, what happens at rotation, restart, concurrency, and recovery boundaries?
- If two nodes say they run the same deployment, can I verify the load-bearing bytes?
- If an agent says a task completed, who verifies the external effect and under which authority?

That posture is the bridge from shipping automation to shipping systems that can be trusted under operational pressure.

[Back to portfolio](../README.md) · [How I Work](../HOW_I_WORK.md) · [Governed deployment](../DEPLOYMENTS/02-governed-agent-execution.md)

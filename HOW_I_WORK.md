# How I Work

## Forward Deployed Engineering Operating Model

The job is not to deliver an AI demo. The job is to understand the operating problem well enough to ship a useful system, make its behavior observable, harden the failure paths, and feed the recurring lessons back into a reusable platform.

My default loop is:

```text
Discover -> Scope -> Build -> Integrate -> Ship -> Observe -> Evaluate -> Harden -> Extract
```

Each stage has a different purpose. Skipping stages usually creates hidden cost later.

---

## 1. Discover the Real Constraint

I start with the workflow, not the model.

Questions I care about:

- What is the user trying to accomplish?
- Where does work stall, leak, duplicate, or fail?
- What is currently manual?
- Which action has the largest business consequence?
- Which systems already own state?
- Where do credentials, permissions, approvals, or compliance constraints live?
- What would make the deployment obviously useful in the first week?

The output is not a feature list. It is a small set of falsifiable statements about the problem.

**Example:** "We need an AI lead agent" is not a useful requirement. "100+ inbound leads arrive every week, only ~40 receive timely contact, and hot leads need first contact inside 15 minutes" is.

---

## 2. Scope a Complete Vertical Slice

I prefer one end-to-end path over several disconnected components.

A useful slice includes the minimum required pieces of:

```text
input -> state -> decision -> action -> evidence -> operator recovery
```

If a proposal has a model but no state owner, an action but no authority boundary, or an automation but no recovery path, it is not complete.

I explicitly separate:

- must-have field behavior;
- temporary integration glue;
- reusable platform candidates;
- deferred ideas.

That prevents premature abstraction from consuming the deployment.

---

## 3. Integrate With the Existing Environment

Forward-deployed work usually fails at the seams, not in the model call.

The important integration questions are things like:

- Which system is authoritative for customer state?
- Is the CRM eventually consistent or transactionally updated?
- What happens when a webhook arrives twice?
- What can retry safely?
- What is the idempotency key?
- Can the agent write anywhere, or only to a scoped target?
- What happens when a provider succeeds but the downstream action fails?
- What does the operator see when the system is degraded?

I use the smallest dependency set that fits the deployment. New infrastructure has to earn its place.

---

## 4. Put Authority Around External Effects

A model can propose an action. That does not mean the action is authorized.

For tool-capable systems I want the external effect path to make these things explicit:

- caller identity;
- requested capability;
- target scope;
- approval requirements;
- budget or quota constraints;
- policy/version identity;
- durable decision evidence.

The principle is simple:

> Prediction is not permission.

This is why my agent work increasingly separates the model/runtime from the authorization and verification boundaries around it.

---

## 5. Ship With Observability, Not Hope

I do not treat a green HTTP response as operational truth.

A deployment should expose enough information to answer:

- Did the workflow start?
- What state is it in?
- What dependency failed?
- What action was attempted?
- Was that action authorized?
- Was the effect actually emitted?
- Did a retry occur?
- Can an operator recover it without guessing?

The difference between telemetry and evidence matters. Logs help explain behavior. Evidence supports a specific claim about what happened.

---

## 6. Evaluate the System, Not Just the Model

A provider response can be valid while the system is still wrong.

I evaluate at the runtime boundary:

- state transitions;
- tool selection;
- fault handling;
- retry behavior;
- continuity across restart/reset;
- side-effect control;
- evidence integrity;
- verifier outcomes.

Where possible, I use deterministic fixtures first so failures are attributable. Live-model variation comes after the harness can already prove its own measurement path.

This is the motivation behind the Runtime Wind Tunnel work.

---

## 7. Convert Incidents Into Controls

An incident is useful only if the system becomes harder to break afterward.

My preferred loop is:

```text
incident -> reproduce -> isolate failure mode -> add control -> add regression proof
```

Examples from this portfolio:

- a health endpoint reported `ok` while its database dependency was unavailable for six days -> split health from readiness and test both failure directions;
- a hash-chained audit trail restarted after log rotation -> anchor rotation to durable prior state and add rotation regression tests;
- an ephemeral container patch disappeared on recreation -> add startup fingerprints for load-bearing code paths.

See [`FIELD-NOTES/production-incidents.md`](FIELD-NOTES/production-incidents.md).

---

## 8. Make Failure Explicit

I prefer explicit degraded states over silent fallbacks.

A fallback is useful when it preserves service. It is dangerous when it hides the fact that the system is no longer operating under the same assumptions.

Good fallback behavior is:

- bounded;
- observable;
- attributable;
- reversible;
- tested.

The operator should be able to tell which path actually ran.

---

## 9. Extract Platform Capability Only After Recurrence

Field work creates pressure to generalize too early.

I do not want a platform abstraction because it looks elegant. I want it because multiple deployments have proven the same constraint is real.

The sequence is:

```text
one-off field fix
  -> repeated pattern
  -> stable interface
  -> reusable primitive
  -> platform capability
```

That is how a deployment teaches the product team what deserves to become product.

Examples include:

- authorization/write-scope enforcement extracted from tool-capable agent work;
- runtime health and drift checks extracted from incidents;
- deterministic conversation state and handoff primitives extracted from voice deployments;
- independent verification and evidence bundles extracted from runtime-evaluation work.

---

## 10. State Maturity Precisely

I do not use "done" as a catch-all.

I distinguish:

| Term | Meaning |
|---|---|
| **Implemented** | The code or configuration exists. |
| **Tested** | Defined behavior has automated checks. |
| **Verified** | Evidence supports the property being claimed. |
| **Accepted** | The designated verifier/gate has authorized the result. |
| **Deployed** | The system is operating in the intended environment. |

This keeps prototypes from being represented as production systems and prevents test completion from being mistaken for business acceptance.

---

## My Default Engineering Biases

- Small vertical slices over broad rewrites.
- Explicit state ownership over hidden coordination.
- Deterministic controls over prompt-only safety.
- Minimal dependencies over infrastructure fashion.
- Local-first when it improves cost/control; cloud when it improves the actual deployment.
- Fail-closed authorization over permissive fallback.
- Bounded retries over unbounded recovery loops.
- Reproducible evidence over unsupported completion claims.
- Reversible changes over migrations with unclear rollback.
- Field value first; platform extraction second.

---

## The Outcome I Optimize For

A successful forward-deployed engagement should leave behind three things:

1. **A working customer outcome** — the business process is materially better.
2. **A hardened deployment** — the important failure modes are observable and bounded.
3. **A reusable lesson** — the platform/product team learned what should be standardized next.

That is the bridge I want to own.

[Back to portfolio](README.md) · [Forward Deployed Playbook](PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md) · [Deployments](DEPLOYMENTS/01-real-estate-lead-operations.md)

<div align="center">

# Gabe Acosta | Forward Deployed Engineer

### Applied AI & Agent Systems

I turn ambiguous operating problems into deployed AI systems, then turn the repeated parts into reusable infrastructure.

[Deployments](#deployment-proof) · [Resume](RESUME.md) · [How I Work](HOW_I_WORK.md) · [Forward Deployed Playbook](PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md) · [Field Notes](FIELD-NOTES/production-incidents.md)

</div>

---

## The Work

Forward deployed engineering is not model demos or architecture theater. It is the full path from a customer problem to a system that survives contact with production:

```text
customer problem
  -> discovery
  -> technical scope
  -> integration
  -> production
  -> evaluation
  -> hardening
  -> measurable impact
  -> reusable platform capability
```

That is how I build.

I work across AI agents, voice systems, workflow automation, local inference, MCP/tool execution, verification, runtime reliability, and the business systems around them. The common pattern is the same: enter a messy environment, find the load-bearing constraint, ship the smallest useful vertical slice, instrument it, pressure-test it, and extract only the primitives worth reusing.

**The deployments are the story. The repos are the evidence.**

---

## Deployment Proof

### 01 — Real-Estate Lead Operations

**Problem:** a solo operator was manually reviewing 100+ inbound leads per week; only about 40 were being contacted and the rest were aging out.

**Deployed:** webhook ingestion, normalization, lead scoring, tier-based routing, voice-agent outreach, CRM sync, local inference, and fallback paths.

**Reported operating outcome:** 100+ leads/week contacted, hot-lead first contact under 15 minutes, manual qualification reduced to zero for the automated path, and uncontacted lead leakage reduced below 5%.

[Read the deployment →](DEPLOYMENTS/01-real-estate-lead-operations.md)

### 02 — Governed Agent Execution

**Problem:** tool-capable agents need authorization and evidence before external actions, not just logs after the fact.

**Deployed capability:** HMAC-signed envelopes, capability-based policy checks, write-scope enforcement, approval boundaries, hash-chained audit evidence, rotation safety, and TOCTOU-safe concurrent writes.

**Public proof:** [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine) exposes the enforcement slice with 14 tests covering the published behavior.

[Read the deployment →](DEPLOYMENTS/02-governed-agent-execution.md)

### 03 — Runtime Wind Tunnel

**Problem:** runtime claims are hard to compare when the model, harness, fault, verifier, and evidence path all move at once.

**Built:** a deterministic two-arm experiment harness around Runtime Lab Specimen 001 with native and governed boundaries, explicit fault schedules, independent verification, append-once evidence bundles, and verification-only replay.

**Public proof:** [`agent-runtime-wind-tunnel`](specimens/agent-runtime-wind-tunnel/) is a zero-key runnable specimen with 14 tests, a six-cell native/governed matrix, real transient-state reset and durable recovery, linked governance receipts, exact eight-file evidence bundles, verification-only replay, and deliberate tamper detection.

**Current boundary:** the private Runtime Lab harness remains fixture-only and not deployed; the public specimen is independently runnable and intentionally smaller. Neither is presented as a model-quality benchmark.

[Run the public specimen →](specimens/agent-runtime-wind-tunnel/) · [Read the deployment →](DEPLOYMENTS/03-runtime-wind-tunnel.md)

---

## Evidence Map

| Capability | Evidence | What it demonstrates |
|---|---|---|
| Voice-agent orchestration | [`voxmaestro`](https://github.com/gabeacosta/voxmaestro) | YAML state machines, tool bridges, filler gates, handoff protocol, runtime boundaries |
| Agent authorization | [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine) | Signed envelopes, capability policy, write scopes, tamper-evident audit chain |
| Runtime experimentation | [`agent-runtime-wind-tunnel`](specimens/agent-runtime-wind-tunnel/) | Runnable controlled-fault specimen: native/governed parity, durable recovery, independent verdicts, replay/tamper verification |
| Runtime reliability | [`clue-runtime`](https://github.com/gabeacosta/clue-runtime) | Dependency-aware readiness and startup drift fingerprinting extracted from incidents |
| MCP configuration diagnostics | [`mcp-audit-plugin`](https://github.com/gabeacosta/mcp-audit-plugin) | Practical MCP audit tooling |
| Multi-tenant state | [`agentic-crm-os`](https://github.com/gabeacosta/agentic-crm-os) | PostgreSQL lifecycle state and row-locked transitions |
| Cost-controlled inference | [`smart-ai-router`](https://github.com/gabeacosta/smart-ai-router) | Local-first/provider-routing scaffold, explicitly labeled as incomplete |
| Private runtime workbench | Runtime Lab | Active private implementation; public proof is extracted above rather than exposing the private system |
| Portfolio receipts | [`receipts/`](receipts/) | Public-safe artifacts supporting selected quantitative claims |

The purpose of this map is not to make every repo look finished. It is to make the maturity and proof boundary obvious.

---

## What I Do Forward Deployed

I am most useful when the requirement is still partly operational, partly technical, and not cleanly owned by a single product surface.

I can:

- sit with the workflow and identify the actual failure mode before choosing the stack;
- scope an end-to-end vertical slice instead of a disconnected proof of concept;
- integrate models, tools, APIs, CRMs, queues, databases, voice systems, and local/cloud infrastructure;
- build explicit approval, budget, write-scope, and side-effect boundaries around agents;
- instrument the system so failures become observable evidence rather than anecdotes;
- reproduce incidents and convert them into regression tests or runtime invariants;
- evaluate the system under controlled faults instead of assuming provider success means system success;
- extract reusable platform primitives only after the field implementation proves they are real.

---

## How I Work

My default loop is:

```text
Discover -> Scope -> Build -> Integrate -> Ship -> Observe -> Evaluate -> Harden -> Extract
```

The detailed operating model is in [`HOW_I_WORK.md`](HOW_I_WORK.md), with the reusable field process in [`PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md`](PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md).

A few rules matter more than any particular framework:

- **Field truth over architecture preference.** The deployment decides what is useful.
- **Smallest viable vertical slice.** One complete workflow beats five disconnected components.
- **Provider completion is not acceptance.** Verification and external effects need explicit ownership.
- **Logs are telemetry; evidence proves behavior.** Important claims need reproducible support.
- **Fail closed on authority.** Missing permission must not become implicit permission.
- **No silent fallbacks.** Degradation should be observable and attributable.
- **Productize only after recurrence.** Reuse is earned by repeated field pressure.

---

## Production Lessons

Some of the most valuable work in this portfolio came from incidents rather than greenfield design:

- a health endpoint reported `ok` for six days while its database dependency had never started;
- a hash-chained audit trail silently restarted after log rotation until the chain anchor was corrected;
- an ephemeral container hotfix could disappear on image recreation, motivating startup fingerprinting.

Those incidents became concrete reliability patterns and tests, not just postmortem prose.

[Read the field notes →](FIELD-NOTES/production-incidents.md)

---

## Proof Standard

This repository is a public proof surface, not a complete source dump.

I distinguish:

- **implemented** — code exists;
- **tested** — defined behavior has automated checks;
- **verified** — evidence supports the expected property;
- **accepted** — the designated verifier or gate has authorized the result;
- **deployed** — the system is operating in its intended environment.

Those words are not interchangeable here.

Customer data, credentials, private infrastructure, proprietary policy data, and internal runtime details are intentionally excluded. Where a claim has a public receipt or runnable repo, I link it. Where it does not, I label the boundary.

---

## Role Fit

I am targeting Forward Deployed Engineer / Forward Deployed AI Engineer roles where the job is to move between customer discovery, systems integration, production debugging, applied AI, and platform feedback.

The strongest fit is a team that wants an engineer who can own the distance between **"the customer needs this"** and **"the platform can reliably do this again."**

[Resume →](RESUME.md) · [How to evaluate this portfolio →](APPLY.md)

---

## Contact

- GitHub: [github.com/gabeacosta](https://github.com/gabeacosta)
- Email: gabriel@gentic.pro
- Focus: forward deployed AI, governed agent execution, runtime reliability, voice systems, workflow automation

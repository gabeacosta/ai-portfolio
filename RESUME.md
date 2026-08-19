# Gabe Acosta

## Forward Deployed Engineer — Applied AI & Agent Systems

Las Vegas, NV · [github.com/gabeacosta](https://github.com/gabeacosta) · gabriel@gentic.pro

---

## Summary

Forward deployed engineer and founder-builder focused on turning ambiguous operating problems into production AI systems, then extracting the repeated patterns into reusable infrastructure.

I work across customer discovery, technical scoping, integrations, workflow automation, voice AI, local inference, MCP/tool execution, runtime reliability, verification, and deployment hardening. My strongest work sits at the boundary between a real business process and the platform primitives required to make that process repeatable, observable, and safe.

The operating loop is simple:

```text
customer problem -> discovery -> scope -> integration -> production
-> evaluation -> hardening -> measurable impact -> reusable capability
```

---

## Selected Forward-Deployed Work

### Real-Estate Lead Operations

**Problem:** a solo real-estate operator was manually reviewing 100+ inbound leads per week, with only about 40 actually contacted.

**Built and integrated:** webhook ingestion, normalization, scoring, tier routing, automated voice outreach, CRM synchronization, local inference, TTS, and fallback paths.

**Reported outcomes:**

- 100+ leads/week contacted through the automated path;
- hot-lead first contact under 15 minutes;
- manual qualification reduced to zero for the automated path;
- uncontacted-lead leakage reduced from roughly 60% to below 5%;
- local intent-classification path reduced marginal inference cost to $0 and latency below 200 ms in the documented evaluation path.

**Evidence:** [deployment write-up](DEPLOYMENTS/01-real-estate-lead-operations.md), [case studies](CASE_STUDIES.md), [VSAI receipt](receipts/vsai_eval_summary.md).

### Governed Agent Execution

**Problem:** agents with tool access can affect files, systems, money, and customer communication; authorization cannot be delegated to model intent or reconstructed from logs after the action.

**Built:** capability-based authorization, HMAC-signed request envelopes, write-scope enforcement, approval boundaries, tamper-evident hash chaining, rotation-safe chain anchoring, and TOCTOU-safe concurrent audit writes.

**Engineering result:** a production incident exposed an audit-chain reset across rotation; the fix converted the failure into regression coverage. The public-safe enforcement slice currently exposes 14 tests for its published behavior.

**Evidence:** [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine), [deployment write-up](DEPLOYMENTS/02-governed-agent-execution.md).

### Runtime Wind Tunnel

**Problem:** runtime and governance claims are difficult to evaluate when model output, runtime behavior, fault injection, verification, and evidence collection are conflated.

**Built:** a deterministic experiment harness for Runtime Lab Specimen 001 with native and governed arms; baseline, constrained context-reset, and contradiction scenarios; immutable fixture checks; independent verdicts; append-once evidence bundles; and replay with side effects disabled.

**Public proof:** extracted a zero-key synthetic specimen that runs the same six-cell native/governed comparison in public, includes a real transient-state destruction/recovery path, emits linked governed receipts and exact eight-file evidence bundles, and fails verification after deliberate evidence tampering. The dependency-free suite passed 14/14 tests before publication.

**Engineering boundary:** the private harness remains fixture-backed and not deployed; the public specimen is runnable but intentionally not a production runtime or live-provider/model-quality benchmark.

**Evidence:** [run the public Wind Tunnel specimen](specimens/agent-runtime-wind-tunnel/), [deployment write-up](DEPLOYMENTS/03-runtime-wind-tunnel.md).

### Voice-Agent Orchestration

**Built:** VoxMaestro, an open-source YAML-driven voice-agent conductor with deterministic state transitions, pre-LLM filler gates, mid-call tool bridging, a three-phase human handoff protocol, guardrails, and an early Pipecat adapter.

**Evidence:** [`voxmaestro`](https://github.com/gabeacosta/voxmaestro).

### Runtime Reliability Patterns

**Incidents converted into reusable controls:**

- dependency-aware health/readiness checks after a service reported healthy for six days while its database dependency was down;
- startup fingerprints to detect container/image drift after ephemeral hotfixes disappeared on recreation.

**Evidence:** [`clue-runtime`](https://github.com/gabeacosta/clue-runtime), [field notes](FIELD-NOTES/production-incidents.md).

---

## Technical Capabilities

**Applied AI / models**
- local inference with MLX and Ollama;
- Qwen-family small-model fine-tuning with LoRA;
- multi-provider LLM routing and fallback design;
- RAG/vector search with Qdrant;
- deterministic fixture-backed model evaluation.

**Agents / runtimes**
- tool-capable agent orchestration;
- MCP gateways and policy enforcement;
- approval boundaries and scoped authority;
- receipt/evidence design;
- deterministic state machines;
- fault injection and independent verification;
- crash/restart and continuity testing.

**Voice / workflow systems**
- voice-agent state machines and handoff protocols;
- STT/TTS integration;
- Twilio/Bland-style telephony integration patterns;
- n8n and webhook-driven automation;
- CRM ingestion and lifecycle automation.

**Infrastructure / data**
- Python, TypeScript/Node.js, Bash, SQL;
- FastAPI, Docker, PostgreSQL, Redis, SQLite;
- local + cloud hybrid deployment;
- HMAC request signing and tamper-evident audit chains;
- structured observability and operational diagnostics.

---

## Public Engineering Proof

| Repository / surface | Proof surface |
|---|---|
| [`voxmaestro`](https://github.com/gabeacosta/voxmaestro) | Full public voice orchestration project |
| [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine) | Public-safe governed execution slice; 14 published tests |
| [`agent-runtime-wind-tunnel`](specimens/agent-runtime-wind-tunnel/) | Runnable zero-key runtime-evaluation specimen; 14-test suite, six-cell fault matrix, durable recovery, replay/tamper verification |
| [`clue-runtime`](https://github.com/gabeacosta/clue-runtime) | Incident-derived runtime reliability patterns; 12 published tests |
| [`mcp-audit-plugin`](https://github.com/gabeacosta/mcp-audit-plugin) | MCP configuration audit tooling |
| [`agentic-crm-os`](https://github.com/gabeacosta/agentic-crm-os) | Multi-tenant PostgreSQL state/lifecycle reference |
| [`ai-portfolio`](https://github.com/gabeacosta/ai-portfolio) | Deployment narratives, field notes, receipts, and proof map |

Private systems and active experiments are described only to the level that can be supported without exposing customer data, credentials, proprietary policy data, or internal infrastructure.

---

## How I Operate

- Start from the field constraint, not the preferred architecture.
- Scope the smallest end-to-end workflow that can create or protect real value.
- Integrate before abstracting.
- Instrument before declaring success.
- Separate model output from authorization and acceptance.
- Reproduce incidents and turn them into tests, invariants, or explicit runbooks.
- Make degradation observable; avoid silent fallback.
- Productize only after the same field problem appears often enough to justify a platform primitive.

Detailed process: [`HOW_I_WORK.md`](HOW_I_WORK.md) and [`PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md`](PLAYBOOKS/FORWARD_DEPLOYED_PLAYBOOK.md).

---

## Target Roles

- Forward Deployed Engineer
- Forward Deployed AI Engineer
- Applied AI Engineer
- AI Infrastructure / Agent Systems Engineer
- Solutions Engineer roles with substantial implementation ownership

I am most interested in roles where I can move from customer context to production implementation and feed the resulting lessons directly back into the product or platform.

# Gabe Acosta

## Forward Deployed Engineer — Applied AI & Agent Systems

Las Vegas, NV · [github.com/gabeacosta](https://github.com/gabeacosta) · gabriel@gentic.pro

---

## Summary

Forward deployed engineer and founder-builder focused on integrating AI into operating workflows and extracting reusable infrastructure from the resulting field lessons. Public work spans deployment accounts, published code slices, and runnable synthetic experiments.

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
- local intent classification on Ollama, with 95.5%→100% cold-set accuracy reported after prefix normalization; the same summary reports weaker adversarial-set results.

The throughput and contact figures are historical operator reports without published execution logs or a measurement window. The accuracy summary does not measure latency or cost savings. Local execution avoids per-request cloud inference charges on that path; hardware, electricity, and operations remain costs.

**Public material:** [deployment account](DEPLOYMENTS/01-real-estate-lead-operations.md), [case studies](CASE_STUDIES.md), [VSAI evaluation summary](receipts/vsai_eval_summary.md), [evidence guide](receipts/README.md).

### Governed Agent Execution

**Problem:** agents with tool access can affect files, systems, money, and customer communication; authorization cannot be delegated to model intent or reconstructed from logs after the action.

**Engineering work:** capability-based authorization, HMAC-signed request envelopes, write-scope enforcement, approval boundaries, hash-chained audit records, rotation continuity, and serialized concurrent audit writes. The public repository contains selected mechanisms and a gateway excerpt; it is not a complete runnable policy service.

**Engineering result:** the published incident account describes an audit-chain reset across rotation and its regression fix. The public slice contains 14 test functions covering write scope (10), rotation continuity (2), and audit concurrency/serialization (2). Those tests do not establish HMAC, role-policy, or full-service coverage.

**Evidence:** [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine), [deployment write-up](DEPLOYMENTS/02-governed-agent-execution.md).

### Runtime Wind Tunnel

**Problem:** runtime and governance claims are difficult to evaluate when model output, runtime behavior, fault injection, verification, and evidence collection are conflated.

**Built:** a deterministic experiment harness for Runtime Lab Specimen 001 with native and governed arms; baseline, constrained context-reset, and contradiction scenarios; immutable fixture checks; independent verdicts; append-once evidence bundles; and replay with side effects disabled.

**Runnable public specimen:** a zero-key synthetic experiment compares native and governed arms across six cells, destroys and recovers transient state, emits linked hash-chained records and eight-file evidence bundles, and detects deliberate evidence tampering during verification-only replay. Its dependency-free suite contains 14 tests.

**Engineering boundary:** the 2026-08-19 portfolio snapshot describes the private harness as fixture-backed and not deployed; the public specimen is runnable but intentionally not a production runtime or live-provider/model-quality benchmark.

**Evidence:** [run the public Wind Tunnel specimen](specimens/agent-runtime-wind-tunnel/), [deployment write-up](DEPLOYMENTS/03-runtime-wind-tunnel.md).

### Voice-Agent Orchestration

**Built:** VoxMaestro, a public alpha YAML-driven voice-agent conductor with deterministic state transitions, pre-LLM filler gates, mid-call tool bridging, a three-phase human handoff protocol, guardrails, and an early Pipecat adapter.

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

## Public Engineering Surfaces

| Repository / surface | Scope |
|---|---|
| [`voxmaestro`](https://github.com/gabeacosta/voxmaestro) | Published voice orchestration project with an early Pipecat adapter |
| [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine) | Enforcement excerpts; 14 tests for write scope, rotation, and audit serialization; gateway needs omitted runtime dependencies |
| [`agent-runtime-wind-tunnel`](specimens/agent-runtime-wind-tunnel/) | Runnable zero-key runtime-evaluation specimen; 14-test suite, six-cell fault matrix, durable recovery, replay/tamper verification |
| [`clue-runtime`](https://github.com/gabeacosta/clue-runtime) | Published incident-derived runtime reliability patterns |
| [`mcp-audit-plugin`](https://github.com/gabeacosta/mcp-audit-plugin) | MCP configuration diagnostic prototype |
| [`agentic-crm-os`](https://github.com/gabeacosta/agentic-crm-os) | Multi-tenant PostgreSQL state/lifecycle reference |
| [`ai-portfolio`](https://github.com/gabeacosta/ai-portfolio) | Deployment narratives, field notes, evidence summaries, and project map |

Deployment narratives describe reported operating experience. Public code and tests support the specific mechanisms they include; the [evidence guide](receipts/README.md) explains what the summary artifacts establish.

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

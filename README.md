<div align="center">

# Gabe Acosta | AI Infrastructure Engineer

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MLX](https://img.shields.io/badge/MLX-000000?style=flat-square&logo=apple&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-ffffff?style=flat-square&logoColor=black)

Voice AI, agent orchestration, and the governance layer underneath both.

[Receipts](receipts/) | [Case Studies](CASE_STUDIES.md) | [Resume](RESUME.md) | [How I Work](HOW_I_WORK.md)

</div>

---

## Start Here

Three things to look at, in order of "fastest to verify yourself":

1. **[`voxmaestro`](https://github.com/gabeacosta/voxmaestro)** — YAML-driven voice agent conductor. Full public repo, Apache-2.0, `pip install voxmaestro` and run it. Not a slice of something bigger — this is the whole thing.
2. **[`mcp-audit-plugin`](https://github.com/gabeacosta/mcp-audit-plugin)** — a Claude Code plugin that audits MCP server configs for performance issues. Install it and point it at your own MCP setup.
3. **[`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine)** and **[`clue-runtime`](https://github.com/gabeacosta/clue-runtime)** — curated, tested slices of the private systems that actually run the businesses below. Each README explains exactly what's excluded and why; each has a green CI badge you can click through to a real run, not a static image.

If you only have two minutes: clone `voxmaestro`, it's the fastest thing here to verify with your own hands.

---

## What I Build

| Domain | What to look for | Where |
|---|---|---|
| Governed agent authorization | HMAC envelopes, RBAC, hash-chained tamper-evident audit log | [`governed-mcp-spine`](https://github.com/gabeacosta/governed-mcp-spine) — 14/14 tests passing in CI |
| Agent-runtime reliability patterns | Health checks that can't lie about dependencies, startup drift fingerprinting | [`clue-runtime`](https://github.com/gabeacosta/clue-runtime) — 12/12 tests passing in CI |
| Voice-agent orchestration | Deterministic state control, filler gates, handoff protocol | [`voxmaestro`](https://github.com/gabeacosta/voxmaestro) |
| Multi-tenant data layer | Postgres state machine with row-locked concurrent transitions | [`agentic-crm-os`](https://github.com/gabeacosta/agentic-crm-os) |
| Cost-controlled inference | Local-first routing, provider fallback | [`smart-ai-router`](https://github.com/gabeacosta/smart-ai-router) — honestly labeled scaffold, not yet package-hardened |
| Business scoring methodology | iRELOP formula weights, tier thresholds, one worked example | [`receipts/score_receipt_example.json`](receipts/score_receipt_example.json) |

This portfolio is a public trust surface, not a complete source dump. Proprietary scoring formulas, customer data, credentials, private URLs, internal IPs, and private infrastructure details are intentionally excluded. Every repo linked above is real, public, and — where it has tests — green in CI at time of writing; check the badge, not this sentence.

---

## Repo Truth Map

| Type | Meaning | Repos |
|---|---|---|
| Owned product, full public mirror | Built as part of this stack, published as-is (secret-scanned, no redaction needed) | `voxmaestro` |
| Owned product, redacted public slice | A curated, secret-scanned subset of a larger private system — see each repo's own "What's not here" section | `governed-mcp-spine`, `clue-runtime` |
| Owned product, schema/data-layer reference | Real, tested code; no application server | `agentic-crm-os` |
| Public scaffold, honestly labeled | Real but incomplete — the repo's own README says so | `smart-ai-router` |
| This repo | Portfolio, case studies, receipts | `ai-portfolio` |

Every repo in the table above is real and public under this account today. If a claim elsewhere in this portfolio names a repo not in this table, that's a bug in the portfolio — [open an issue](https://github.com/gabeacosta/ai-portfolio/issues).

---

## Flagship Work

| Project | What it proves | Status |
|---|---|---|
| Governed MCP spine (public slice) | Agents authorize tool calls through capability checks, write-scope enforcement, and a hash-chained audit log — with the concurrency and rotation-safety properties proven by real tests, not asserted | 14/14 tests passing, CI green |
| Clue Runtime (public slice) | Two production-incident-driven reliability patterns: dependency-aware health checks, startup drift fingerprinting | 12/12 tests passing, CI green |
| VoxMaestro | YAML-driven voice orchestration, deterministic state machines, filler gates, handoff protocol | Public alpha, runnable, Apache-2.0 |
| Agentic CRM OS | Multi-tenant lead lifecycle state machine with `FOR UPDATE` row locking — the race-condition-safety claim is demonstrated by an actual concurrency test, not just described | Schema + state machine, tested |

---

## Proof Receipts

See [`receipts/`](receipts/) for public-safe proof artifacts backing the specific numbers used elsewhere in this portfolio.

| Receipt | What it backs |
|---|---|
| [VSAI eval summary](receipts/vsai_eval_summary.md) | The 95.5%→100% intent-classifier accuracy figure, methodology, and known failure modes (including where it does *not* hold — adversarial phrasing) |
| [Local inference cost model](receipts/local_inference_cost_model.md) | The $0-marginal-cost local-inference claim, with explicit assumptions and scale limits |
| [n8n inventory (redacted)](receipts/n8n_inventory_redacted.md) | Workflow categories and design patterns, without credentials or webhook paths |
| [Score receipt example](receipts/score_receipt_example.json) | One worked iRELOP scoring example, consistent with the Case Study 6 figures below |
| [Security sweep (redacted)](receipts/security_sweep_redacted.md) | Secret-scanning, audit-chain integrity, and drift-detection methodology — including two real gaps found and fixed during the most recent audit |

Claims elsewhere in this portfolio that aren't linked to one of these should be read as architecture and operating narrative, not audited production proof — see [`CASE_STUDIES.md`](CASE_STUDIES.md)'s own framing at the top of that document.

---

## How It Fits Together

```text
Ingestion
  Voice transcripts, web forms, CRM events, workflow triggers

Intelligence
  Intent classification, public-safe scoring contracts, RAG, local/cloud LLM routing

Coordination
  Governed MCP spine, policy scopes, budget controls, approval boundaries

Orchestration
  n8n workflows, Postgres state, Redis queues/cache, provider fallback paths

Action
  Voice agents, SMS/email handoff, CRM updates, reporting, alerts
```

The strategy is local-first where possible, cloud where useful, and governed execution wherever a model or agent can affect money, customer communication, or business records.

---

## Case Studies

Case studies should be read as architecture and operating narratives unless a linked receipt proves the metric.

- [Conversation Engine](CASE_STUDIES.md#conversation-engine)
- [Cloud to Local Inference](CASE_STUDIES.md#case-study-1-replacing-cloud-ai-with-local-inference)
- [Cloud to Local TTS](CASE_STUDIES.md#case-study-2-zero-cost-tts-for-multi-language-voice-agents)
- [Manual to Automated Qualification](CASE_STUDIES.md#case-study-3-from-manual-lead-qualification-to-full-automation)
- [Operating Cost Analysis](CASE_STUDIES.md#case-study-4-ai-agent-operating-cost-vs-revenue)

---

## Contact

- GitHub: [github.com/gabeacosta](https://github.com/gabeacosta)
- Email: gabriel@gentic.pro
- Focus: governed MCP infrastructure, tool routing, cost controls, voice agents

# Portfolio audit — 2026-10-30

## Scope

Reviewed the public portfolio at baseline commit `8186416d3f4410a48bcf0afe02353de40b52a5f5`, its Markdown examples, linked public project descriptions, and the checked-in Wind Tunnel specimen. No private infrastructure was inspected, no provider calls were made, and no customer outcomes were remeasured. Existing source evidence summaries and scoring example remain unchanged.

## Corrections

| Finding | Change |
| --- | --- |
| Historical operating reports mixed with reproducible proof | Separate operator reports, code excerpts, reference recipes, and the runnable synthetic specimen |
| Evaluation summary used to imply latency and billing results | Limit the summary to its reported evaluation scope; identify absent timing traces and invoices |
| Local inference conflated distinct runtime paths | Distinguish Ollama classifier evaluation from MLX conversation-engine notes and historical TTS configurations |
| Infrastructure budgets and zero-cost wording overstated economics | Show the historical listed subtotal and unmetered/excluded costs; remove unsupported savings and margin claims |
| Public gateway described as more complete than its source/tests | Identify the unpublished signing helper and the exact published test categories |
| Old APPLY instructions described merging a positioning branch | Replace them with a reviewer path and direct Python specimen commands |
| README-only examples described as production-tested utilities | Label them as reference recipes, correct configuration/examples, and state the orchestration boundary |
| Root-relative receipt links and unfinished follow-up sections | Repair local links and replace placeholders with existing scoped material |
| No explanatory visual assets | Add self-contained inline diagrams to the hub, deployment accounts, six case studies, recipes, specimen, and operating guides |

## Executed verification

Using Python 3.13 in an isolated copy of the public specimen:

| Check | Result | Exit |
| --- | --- | --- |
| `python3.13 -m unittest discover -s tests -v` | 14 tests passed | 0 |
| `python3.13 -m wind_tunnel demo` | Six expected verdicts: baseline/reset VERIFIED; contradiction MISMATCH in both arms | 0 |
| `python3.13 -m wind_tunnel tamper` | Deliberately changed evidence rejected with EVIDENCE_HASH_MISMATCH | 0 |
| `verify` on a pristine evidence bundle | REPLAY_VERIFIED | 0 |
| `verify` on the altered bundle | EVIDENCE_HASH_MISMATCH | 1 |

Each generated bundle had the expected eight files. The recorded scorecards distinguished zero native receipts from two governed receipts. Replay disables simulated effects and performs no provider calls. The tamper demonstration's exit 0 means the expected rejection occurred; it does not mean corrupted evidence verified.

The inline recipe blocks were checked for Python syntax, imports, documented call shapes, and selected behaviors using offline mocked dependencies. No external provider compatibility or production safety claim follows from those checks.

Local Markdown links, fragment targets, SVG structure, image references, and rendered diagram layouts were checked as part of this revision. Diagrams are design summaries, not application screenshots or current operating measurements.

## Public source inspection

The linked [Governed MCP Spine](https://github.com/gabeacosta/governed-mcp-spine) contains 14 test functions: 10 write-scope, 2 rotation-fallback, and 2 serial/concurrent audit-file tests. That suite was inspected, not executed in this audit. Its file-only concurrency replacement does not prove database replication or cross-host ordering. Its HMAC and capability integration are not covered by those 14 tests, and the full public gateway has an unpublished signing dependency.

All eight inspected supporting repository URLs were public and available at the audit date: [VoxMaestro](https://github.com/gabeacosta/voxmaestro), [Governed MCP Spine](https://github.com/gabeacosta/governed-mcp-spine), [Agentic CRM OS](https://github.com/gabeacosta/agentic-crm-os), [Clue Runtime](https://github.com/gabeacosta/clue-runtime), [MCP Audit Plugin](https://github.com/gabeacosta/mcp-audit-plugin), [Smart AI Router](https://github.com/gabeacosta/smart-ai-router), [AgentReceipts](https://github.com/gabeacosta/agentreceipts), and [MiniEval](https://github.com/gabeacosta/minieval). Availability of source is not deployment verification.

## What remains outside this audit

Private deployment status, raw model datasets, actual production latency, invoice-based savings, caller/contact outcomes, and security certification remain outside the public verification boundary. Historical private Runtime Lab descriptions reflect the 2026-08-19 portfolio snapshot.

[Portfolio](../README.md) · [Reviewer guide](../APPLY.md) · [Evidence guide](../receipts/README.md)

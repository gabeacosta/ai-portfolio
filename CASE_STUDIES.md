<div align="center">

# Case Studies

> Real outcomes from production systems. No demos, no proofs-of-concept.

[![Back to Portfolio](https://img.shields.io/badge/Back_to-Portfolio-22c55e?style=flat-square)](README.md)
[![Resume](https://img.shields.io/badge/Resume-view-000?style=flat-square)](RESUME.md)
[![How I Work](https://img.shields.io/badge/How_I_Work-view-8B5CF6?style=flat-square)](HOW_I_WORK.md)

</div>

---

## Case Study 1: Replacing Cloud AI with Local Inference

![Savings](https://img.shields.io/badge/savings-$500%2Fmo-22c55e?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/accuracy-95.5pct_to_100pct-22c55e?style=for-the-badge)
![Latency](https://img.shields.io/badge/latency-%3C200ms-22c55e?style=for-the-badge)

### Challenge
Voice AI operations processing 100+ calls/week were spending $300-500/month on cloud LLM APIs for intent classification alone. Latency averaged 800ms-1.2s per classification, creating awkward pauses in live calls.

### Solution
Fine-tuned Qwen 2.5 1.5B with LoRA on domain-specific voice transcripts. Deployed on local Apple Silicon using MLX inference with Ollama as failback. 3-tier cascade: MLX (primary), Ollama (local fallback), cloud Ollama (remote fallback).

### Results
| Metric | Before | After |
|--------|--------|-------|
| Monthly inference cost | $300-500 | **$0** |
| Classification latency | 800ms-1.2s | **<200ms** |
| Accuracy | ~88% (generic model) | **95.5%→100%** (prefix-normalizer fix, see [receipt](../receipts/vsai_eval_summary.md)) |
| Uptime | Dependent on API provider | **Self-controlled, 3-tier fallback** |

### Key Insight
Small models fine-tuned on domain data consistently beat large general models for classification tasks. The 1.5B parameter model outperforms models 10-50x its size because it learned the specific vocabulary and patterns of real estate lead calls.

---

## Case Study 2: Zero-Cost TTS for Multi-Language Voice Agents

![Savings](https://img.shields.io/badge/savings-$400%2Fmo-22c55e?style=for-the-badge)
![Languages](https://img.shields.io/badge/languages-EN%2FES%2FZH-26A5E4?style=for-the-badge)
![Failover](https://img.shields.io/badge/failover-3_layers-f59e0b?style=for-the-badge)

### Challenge
Cloud TTS services (Google, AWS Polly, ElevenLabs) were charging $0.004-0.016 per 1,000 characters. At scale across EN/ES/ZH calls, monthly TTS costs were projected to hit $200-400/month.

### Solution
Self-hosted Piper + Edge TTS with espeak fallback. Cross-node failover between local and cloud nodes.

### Results
| Metric | Before (Cloud) | After (Self-Hosted) |
|--------|----------------|---------------------|
| Monthly cost | $200-400 projected | **$0** |
| Languages | Depends on provider | **EN, ES, ZH** |
| Failover layers | 1 (provider SLA) | **3 (Piper, Edge TTS, espeak)** |
| Vendor lock-in | High | **None** |

### Key Insight
TTS is a solved problem at the open-source level. Piper voices are indistinguishable from cloud voices in phone-quality audio. Edge TTS provides neural quality at zero cost as a secondary layer.

---

## Case Study 3: From Manual Lead Qualification to Full Automation

![Throughput](https://img.shields.io/badge/throughput-100%2B%2Fweek-22c55e?style=for-the-badge)
![Speed](https://img.shields.io/badge/first_contact-%3C15min-22c55e?style=for-the-badge)
![Leakage](https://img.shields.io/badge/leakage-%3C5%25-22c55e?style=for-the-badge)

### Challenge
A solo real estate investor was manually reviewing 100+ inbound leads per week. Each lead required 5-10 minutes of research and a phone call to qualify. Effective capacity: ~40 leads/week actually contacted, 60+ going cold.

### Solution
End-to-end automated pipeline: webhook ingestion, data normalization, iRELOP scoring (100-point proprietary model), tier-based routing, automated voice agent outreach for warm/cool tiers, immediate callback routing for hot leads. CRM sync to HubSpot with auto-deal creation.

### Results
| Metric | Before | After |
|--------|--------|-------|
| Leads contacted/week | ~40 | **100+** |
| Time to first contact | 2-48 hours | **<15 minutes (hot), <2 hours (warm)** |
| Manual qualification time | 5-10 min/lead | **0 (automated)** |
| Lead leakage (uncontacted) | ~60% | **<5%** |

### Key Insight
Speed-to-contact is the single biggest predictor of deal conversion in real estate. Automating the qualification and first-touch process fundamentally changes conversion rates because leads are contacted while still motivated.

---

## Case Study 4: AI Agent Operating Cost vs. Revenue

![Infra Cost](https://img.shields.io/badge/infra-$15%2Fmo-22c55e?style=for-the-badge)
![Margin](https://img.shields.io/badge/margin-%3C2%25_of_revenue-22c55e?style=for-the-badge)
![Products](https://img.shields.io/badge/products-18-f59e0b?style=for-the-badge)

### Challenge
Demonstrate that a full AI automation stack can operate at costs low enough to serve SMBs profitably at accessible price points.

### Solution
Architect everything local-first with cloud as fallback only. Own compute hardware, use open-source models, self-host all services.

### Monthly Operating Cost Breakdown
| Service | Cost |
|---------|------|
| Cloud hosting | ~$12 |
| Domain/SSL | ~$1 |
| Cloud LLM (fallback only) | ~$5-15 |
| Voice (Bland AI/Twilio, per-use) | Variable |
| Everything else | $0 (self-hosted) |
| **Total fixed infrastructure** | **~$15-30/month** |

### Revenue per Client
| Product | Monthly |
|---------|---------|
| Growth Engine | $1,497 |
| Lead Recovery | $2,497 |
| Arachne Claw (self-serve) | $50 |

### Margin
Infrastructure cost is <2% of revenue per client. Even at a single client, the unit economics work. At 30 clients ($57K MRR target), infrastructure is a rounding error.

### Key Insight
The competitive moat is the cost structure, not the AI itself. Competitors running on cloud-everything pay 10-20x more in infrastructure, which either eats their margin or forces higher prices. Local-first architecture turns infrastructure into a profit center.

---

## Case Study 5: Multi-Agent Coordination with Tiered Autonomy

![Architecture](https://img.shields.io/badge/architecture-novel-8B5CF6?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-2_coordinated-22c55e?style=for-the-badge)
![Autonomy](https://img.shields.io/badge/tiers-4_levels-f59e0b?style=for-the-badge)

### Challenge
Two production AI agents — an orchestrator and a tactical executor — needed to coordinate on lead processing, voice calls, and deal analysis without stepping on each other. Direct webhook messaging was fragile, with no conflict resolution or approval gates for sensitive actions.

### Solution
Built Markspace, a stigmergy-based coordination protocol. Agents write "marks" (intents, actions, observations) into a shared space. A Guard enforces identity and permissions per scope. Outbound calls/SMS require human approval via Telegram inline keyboard. Four autonomy tiers control what agents can do without human oversight.

### Results
| Metric | Before | After |
|--------|--------|-------|
| Coordination method | Direct webhooks | **Stigmergy (decoupled)** |
| Conflict resolution | None (race conditions) | **FIRST_WRITER / HIGHEST_CONFIDENCE policies** |
| Outbound call safety | Manually triggered | **Tiered: autonomous for scoring, approval-gated for calls** |
| Audit trail | Partial logs | **Every action mark persisted to PostgreSQL** |

### Key Insight
Agent coordination is an infrastructure problem, not an AI problem. The agents don't need to "understand" each other. They need a shared space with enforced rules. Stigmergy (indirect coordination through environment marks) is simpler and more robust than direct agent-to-agent messaging.

---

## Case Study 6: Zero-Cost Lead Enrichment Pipeline

![Savings](https://img.shields.io/badge/savings-$200%2Fmo-22c55e?style=for-the-badge)
![Cost](https://img.shields.io/badge/cost-$0%2Fmo-22c55e?style=for-the-badge)
![Markets](https://img.shields.io/badge/markets-NV%2FAZ%2FFL%2FNC%2FSC%2FTX-f59e0b?style=for-the-badge)

### Challenge
The iRELOP lead scoring pipeline needed property data (estimated value, equity, years owned, tax info) to score HOT/WARM/COOL/PASS tiers. The commercial solution (BatchData API) costs $200+/month with minimum commitments. County APIs returned HTML, not JSON. Zillow and Redfin blocked server-side requests. ATTOM required an enterprise key.

### Solution
Built `prop-enricher`: a FastAPI microservice wrapping HomeHarvest, an open-source Realtor.com scraper requiring no API key. Deployed as a Docker container on the VPS. Added a 30-year amortization equity model (10% down, 6.5% rate) to derive estimated equity from purchase price. Semaphore-serialized requests to avoid rate limiting.

### Results
| Metric | Before | After |
|--------|--------|-------|
| Monthly enrichment cost | $200+ (BatchData) | **$0** |
| Data sources explored | Zillow, Redfin, ATTOM, Maricopa, Propwire | **Realtor.com via HomeHarvest** |
| Markets covered | Depends on paid tier | **NV, AZ, FL, NC, SC, TX** |
| Pipeline uptime | API dependency | **Self-hosted, no key required** |
| Time to first HOT lead | Manual flags required | **Automatic enrichment + override support** |

### Smoke Test Results
| Lead | Score | Tier | Telegram Alert |
|------|-------|------|----------------|
| Auto-enriched (Pahrump, NV) | 29 | PASS | — |
| Manual override (tax + pre_foreclosure) | 59 | COOL | — |
| High equity + tax delinquent | 77 | WARM | — |
| Tax + pre + absentee flags | 95 | HOT | ✅ Fired |

### Key Insight
Paid data APIs are the default assumption in RE tech, but most of the signals needed for early-funnel qualification are available via public scrapers. The motivation flags (tax_delinquent, pre_foreclosure) that push a lead to HOT often come from the intake form itself — from the person dispatching the lead. Paid data becomes valuable at scale; at <100 leads/week it's just overhead.

---

## Conversation Engine + iRELOP Lead Scoring {#conversation-engine}

<!-- TODO: Gabe to fill — target structure:
- Problem (what was being done manually / what cloud API was costing)
- Approach (why inline directives vs. function calling, why local model)
- Architecture (state tracker, training pipeline, scoring routing)
- Outcome (real numbers: leads processed, accuracy, cost replaced)
- What I'd do differently
-->

> **Covered in brief:** See [Case Study 1](#case-study-1-replacing-cloud-ai-with-local-inference) and [Case Study 3](#case-study-3-from-manual-lead-qualification-to-full-automation) above for the inference and pipeline outcomes. Full deep-dive coming.

---

## Ceiba Core — Agent Execution Control Plane {#ceiba-core}

<!-- TODO: Gabe to fill — target structure:
- Problem (agents executing without oversight, blast radius issue)
- Approach (policy plane vs. hardcoded guards)
- Architecture (Redis gateway, policy DSL, approval webhooks)
- Outcome (number of policy hits, agents using it, false-positive rate)
- What I'd do differently
-->

---

## Arachne Swarm — Multi-Agent Orchestration {#arachne-swarm}

<!-- TODO: Gabe to fill — target structure:
- Problem (webhook spaghetti at 3+ agents)
- Approach (stigmergy / Markspace, why it scales)
- Architecture (mark types, guard scopes, conflict resolution)
- Outcome (agents coordinated, conflicts auto-resolved)
- What I'd do differently
-->

> **Covered in brief:** See [Case Study 5](#case-study-5-multi-agent-coordination-with-tiered-autonomy) above for the coordination architecture and outcomes. Full deep-dive coming.

---

<div align="center">

[![Back to Portfolio](https://img.shields.io/badge/Back_to-Portfolio-22c55e?style=for-the-badge)](README.md)
[![Resume](https://img.shields.io/badge/Resume-view-000?style=for-the-badge)](RESUME.md)

</div>

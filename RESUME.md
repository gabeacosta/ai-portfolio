<div align="center">

# Gabe Acosta

### AI Infrastructure Engineer & Automation Architect

![AI/ML](https://img.shields.io/badge/AI%2FML-Engineering-22c55e?style=for-the-badge)
![Voice AI](https://img.shields.io/badge/Voice-AI-26A5E4?style=for-the-badge)
![Agents](https://img.shields.io/badge/Multi--Agent-Orchestration-8B5CF6?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Architecture-EA4B71?style=for-the-badge)

> I build production AI systems that run at $0/month and generate revenue from day one.

[![Portfolio](https://img.shields.io/badge/Portfolio-README-22c55e?style=flat-square)](README.md)
[![Case Studies](https://img.shields.io/badge/Case_Studies-6_studies-f59e0b?style=flat-square)](CASE_STUDIES.md)
[![How I Work](https://img.shields.io/badge/How_I_Work-8_principles-8B5CF6?style=flat-square)](HOW_I_WORK.md)
[![Email](https://img.shields.io/badge/Email-gabriel%40gentic.pro-blue?style=flat-square)](mailto:gabriel@gentic.pro)

</div>

---

## Core Competencies

<table>
<tr>
<td width="50%">

**AI/ML Engineering**
![LoRA](https://img.shields.io/badge/LoRA-Qwen_2.5-FF6F00?style=flat-square)
![MLX](https://img.shields.io/badge/MLX-inference-000?style=flat-square&logo=apple&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-RAG-24B47E?style=flat-square)

Fine-tuning small language models, custom inference pipelines (MLX, Ollama), multi-provider LLM routing with complexity-based model selection, RAG systems, vector search

</td>
<td width="50%">

**AI Agent Orchestration**
![Markspace](https://img.shields.io/badge/Markspace-stigmergy-8B5CF6?style=flat-square)
![Arachne](https://img.shields.io/badge/Arachne-swarm-22c55e?style=flat-square)

Multi-agent coordination (Markspace protocol), tiered autonomy models, agent fleet management (Arachne Swarm), SaaS agent platforms (Arachne Claw)

</td>
</tr>
<tr>
<td width="50%">

**Voice AI**
![Bland](https://img.shields.io/badge/Bland_AI-voice-5046E5?style=flat-square)
![Twilio](https://img.shields.io/badge/Twilio-SMS-F22F46?style=flat-square&logo=twilio&logoColor=white)
![TTS](https://img.shields.io/badge/Piper-TTS-22c55e?style=flat-square)

End-to-end voice agent design, custom TTS (Piper/Edge TTS), real-time intent classification, conversation state management with inline directives

</td>
<td width="50%">

**Automation Architecture**
![n8n](https://img.shields.io/badge/n8n-50%2B_flows-EA4B71?style=flat-square&logo=n8n&logoColor=white)
![Webhooks](https://img.shields.io/badge/webhooks-HMAC-f59e0b?style=flat-square)

66 production workflows, webhook-driven event systems, lead processing pipelines, multi-business orchestration, approval-gated outbound

</td>
</tr>
<tr>
<td width="50%">

**Infrastructure**
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![PG](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)

Docker, Traefik SSL, PostgreSQL, Redis, local + cloud hybrid architecture, MCP servers, cost-zero local deployment

</td>
<td width="50%">

**Web Intelligence**
![Scrapling](https://img.shields.io/badge/Scrapling-stealth-f59e0b?style=flat-square)
![Firecrawl](https://img.shields.io/badge/Firecrawl-extract-22c55e?style=flat-square)

Scrapling, Firecrawl, Crawl4AI, anti-bot bypass, adaptive DOM parsing, structured extraction

</td>
</tr>
</table>

---

## What I've Built

### Arachne Platform: Agent Orchestration SaaS (sunset, substrate repurposed)
Full-stack agent management: real-time spider web visualization, Kanban pipeline, budget controls, multi-tenant isolation, Stripe billing, tiered pricing. Next.js, WebSocket, PostgreSQL, Docker. The product was sunset; the substrate is being repurposed as an internal tenant-aware control plane rather than run as a standalone SaaS.

### Markspace Protocol: Multi-Agent Coordination
Novel stigmergy-based coordination replacing direct messaging between AI agents. Guard-enforced identity, 6 scoped domains, 4-tier autonomy (autonomous / notify-then-act / approval-required / blocked). Approval flow via Telegram inline keyboards.

### Custom Intent Classifier. 95.5% → 100% Cold-Eval Accuracy
Fine-tuned Qwen 2.5 1.5B with LoRA for real-time voice call classification. 9-class model, $0/month inference on Apple Silicon. 3-tier cascade: MLX, Ollama, cloud. Outperforms generic classifiers on domain-specific calls.

### Hybrid Compute Platform. $15/month Total
Local compute (ML inference, TTS, scraping, agent brain) + cloud Docker (n8n, databases, reverse proxy, voice relay). Replaces $200-500/month equivalent cloud infrastructure.

### Conversation Engine with Inline Directives
State tracker injects dynamic prompts per-turn instead of static system prompts. Synthetic training pipeline generating 1,500+ multi-turn conversations with adversarial seller personas. Handles evasive and emotionally resistant callers.

### Multi-Language TTS at Zero Cost
Piper + Edge TTS with espeak fallback. Three-layer failover, cross-node recovery between local and cloud. Processes hundreds of calls weekly at $0/month.

### Lead Intelligence Pipeline. 100+ Leads/Week
Proprietary iRELOP scoring (Motivation 40, Opportunity 35, Profile 25), automated tier routing, voice agent outreach, CRM sync (HubSpot). End-to-end from ingestion to disposition.

---

## Technical Stack

| Layer | Technologies |
|-------|-------------|
| Models | Qwen 2.5, MLX, Ollama, LoRA, xAI Grok, Gemini, Claude |
| Agents | Arachne Swarm, Markspace, private orchestrator + executor agents |
| Voice | Bland AI, Twilio, Piper, Edge TTS |
| Orchestration | n8n, webhooks, cron, Docker, Traefik |
| Data | PostgreSQL, Redis, Qdrant, Supabase |
| Scraping | Scrapling, Firecrawl, Crawl4AI, MCP |
| Infra | Local compute, cloud node, reverse proxy SSL, Docker Compose |
| Frontend | Next.js, React, Tailwind, Vercel |
| Languages | Python, TypeScript/Node.js, Bash, SQL |

---

## Businesses Powered by This Stack

**DealiQ**. AI-powered real estate investment across Phoenix, Vegas, AZ, UT. 100+ leads/week through automated qualification and voice agent outreach.

**Gentic AI**. AI automation platform for local SMBs. Growth Engine ($1,497/mo), Lead Recovery ($2,497/mo). Target: $57K MRR.

**VoiceScheduleAI**. AI appointment scheduling with custom voice agents.

**Arachne Claw**. Self-serve AI agent sandbox (7 agent types, dashboard + email delivery, REST API), built as top-of-funnel for Gentic AI. Sunset; substrate being repurposed internally.

---

## What I'm Looking For

- AI/ML infrastructure roles where I own the full stack
- Voice AI and conversational AI engineering
- AI agent orchestration and multi-agent systems
- Automation architecture for AI-first products
- Technical leadership where shipping matters more than meetings
- Contract work on production AI systems

---

<div align="center">

[![Email](https://img.shields.io/badge/gabriel%40gentic.pro-contact-22c55e?style=for-the-badge)](mailto:gabriel@gentic.pro)
[![Portfolio](https://img.shields.io/badge/Portfolio-README-000?style=for-the-badge)](README.md)
[![VoxMaestro](https://img.shields.io/badge/VoxMaestro-pip_install-22c55e?style=for-the-badge)](https://github.com/genticai0910-png/voxmaestro)


</div>

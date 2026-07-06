# n8n Workflow Inventory (redacted)

A production n8n instance running dozens of workflows across the businesses this stack serves. No webhook URLs, credentials, hostnames, or internal IPs below — categories and trigger types only.

## Categories

| Category | Trigger type | Purpose |
|---|---|---|
| Lead ingestion | Webhook | Normalize inbound leads from multiple source types (skip-trace, forms, scrapers) into a common schema |
| Lead scoring | Webhook / internal call | Run the iRELOP scoring model, tier the lead, route by tier |
| Voice outreach | Webhook (call-status callbacks) | Fire outbound voice agent calls, ingest call-completion events, update lead state |
| SMS/email outreach | Schedule + webhook | Templated follow-up sequences with reply-triggered state transitions |
| CRM sync | Webhook | Push qualified leads and status changes to the CRM |
| Data enrichment | Internal call | Property/owner data lookups feeding the scoring model |
| Monitoring/alerting | Schedule (cron) | Health checks, drift detection, and Telegram alerting for the rest of the stack |
| Content/social | Schedule + webhook | Scheduled content generation and multi-platform publishing |

## Design patterns used throughout

- **Dead letter handling**: failed executions land in an error-workflow path rather than silently dropping, so nothing gets lost without a trace.
- **Idempotency**: webhook-triggered workflows dedupe on a stable key (e.g. an inbound webhook's own delivery ID) so retries from the sending system don't double-process.
- **Approval gates**: outbound communication (calls, SMS, email) that could reach a real person passes through an approval check before firing, not immediately on ingestion.

## What's excluded

Exact workflow count, node-level implementation detail, credential names, webhook paths, and which specific business each workflow belongs to are not included here.

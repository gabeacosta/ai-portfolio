# Local Inference Cost Model

## Hardware

Mac Mini M4, 16GB unified memory. Owned hardware, sunk cost — not billed per-request.

## Workload running locally at $0 marginal cost

- Real-time voice-call intent classification (VSAI, Qwen 2.5 1.5B + LoRA) via local Ollama
- Conversation-engine LLM inference (CE model, MLX) for lead-qualification dialogue
- TTS (Kokoro)
- Embeddings (nomic-embed-text) for RAG/vector search

## Cloud fallback (not primary path)

A small cloud LLM tier exists purely as a failover for the above local models and for tasks the local models can't handle (general reasoning, long-context summarization). Cloud calls are the exception path, not the default — the routing logic tries local first, always.

## Assumptions and caveats

- **Electricity is not itemized separately** — folded into "owned hardware" above, not broken out as its own line item. A rigorous cost model would meter it; this one doesn't.
- **This is a single-operator, low-to-moderate call-volume workload** (dozens to low hundreds of calls/week across the businesses this stack serves). The economics of "local beats cloud" shift at high enough volume that GPU cloud instances amortize better than a single Mac Mini — this model does not claim to generalize to that scale.
- **Model quality tradeoff**: a 1.5B fine-tuned model beats a bigger general model on this specific narrow task (domain-specific intent classification — see [`vsai_eval_summary.md`](vsai_eval_summary.md)), but that's a claim specific to narrow, well-defined classification tasks, not a general "small models beat big models" claim.
- **No cloud invoice is published here.** The comparison is architectural (what would this same call volume cost against a metered API, at the fallback tier's own published per-token pricing) rather than a redacted real invoice.

## Bottom line

For this specific workload shape — narrow, high-frequency, well-defined classification and short-form generation tasks, at this specific volume — local-first inference is the right default, with cloud reserved for genuine overflow/complexity cases. The savings are structural (near-zero marginal cost per call) rather than a specific dollar figure this receipt can defend without a metered production invoice to point to.

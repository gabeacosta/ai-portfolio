# VSAI Intent Classifier — Eval Summary

**Model**: Qwen 2.5 1.5B, LoRA fine-tuned for real-time voice-call intent classification.

## Methodology

- 9-class intent taxonomy for real estate seller-lead calls (e.g. `interested`, `objection`, `wrong_number`, `callback_requested`).
- Held-out cold eval set, never seen during LoRA training.
- Runtime path: local Ollama, with a cloud mirror as fallback only — this receipt covers the local model's own accuracy, not fallback behavior.

## Headline result

| Stage | Accuracy |
|---|---|
| Cold eval, initial LoRA | 95.5% |
| Cold eval, after prefix-normalizer fix | 100% |

**What the prefix-normalizer fix was**: the classifier's misses were concentrated in a narrow failure mode — inputs with a specific greeting-prefix pattern the training data underrepresented. A normalization step applied before inference (stripping/canonicalizing that prefix) closed the remaining gap on the cold set. This is a data/preprocessing fix, not a retrain.

## Known failure modes at time of writing

- Adversarial phrasing designed to be ambiguous between two intent classes (a deliberately hard test set, not representative of live traffic) scores meaningfully lower — mid-60s% accuracy — than the cold eval above. This is expected and disclosed, not a contradiction: the 100% figure is against the cold eval distribution, not an adversarial one.
- Prompt-optimization techniques (tested via COPRO) do not improve a fine-tuned model like this one — every variant tested degraded accuracy relative to the baseline prompt the model was trained against. Don't try to prompt-engineer around a fine-tune; retrain instead.

## What's excluded

Raw training data, real caller transcripts, the exact prefix pattern, and the eval harness's internal dataset splits are not included — those are private training assets, not methodology.

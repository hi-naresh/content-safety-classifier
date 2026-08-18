# Content-Safety Classifier with Adversarial Robustness Eval

Safety classifier plus adversarial test loop for keeping the model honest under jailbreak prompts.

## At a glance

- Train a lightweight encoder on a bounded Aegis category set
- Evaluate precision, recall, and F1 per category
- Stress-test the same model with `garak`
- Serve the classifier with FastAPI

## Model side

The classifier is a multi-label text model, not a full LLM fine-tune. The point is to keep the
stack small enough to ship while still measuring whether the safety categories hold up in practice.

## Robustness side

`garak` is the adversarial check. It should tell you whether the model still catches unsafe content
when the prompt is phrased to dodge detection.

## Suggested repo tour

1. `src/data/` for dataset download and label prep
2. `src/model/` for fine-tuning
3. `src/eval/` for held-out metrics and adversarial scoring
4. `src/serve/` for the API layer

## What the finished project should show

Clean-set scores, per-category breakdowns, and a measured robustness drop under jailbreak-style
perturbations, plus a short note on which category was easiest to evade.

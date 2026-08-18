# Content-Safety Classifier with Adversarial Robustness Eval

**Status: scaffolded** — skeleton only, no trained model yet. This repo is the starting point for a
real build session, not a finished project.

## Problem

LLM content-safety classifiers need to flag unsafe outputs across specific, named risk categories
(hate/harassment, sexual, harmful/violent) with high precision and recall, while also holding up
against adversarially-phrased ("jailbreak") attempts to evade detection. This project builds a
lightweight text classifier for that, fine-tuned on an open safety dataset, and stress-tests it
against a jailbreak-prompt suite rather than reporting only clean-set accuracy.

## Named mechanism

Fine-tuning a lightweight transformer encoder (e.g. DeBERTa-v3-small or RoBERTa-base) as a
multi-label classifier over NVIDIA's open Aegis-AI-Content-Safety-Dataset risk taxonomy, evaluated
with per-category precision/recall/F1 on a held-out split, then adversarially stress-tested using
`garak` (NVIDIA's open-source LLM vulnerability scanner) to measure the drop in detection rate under
jailbreak-style prompt perturbations.

## Stack

Python, PyTorch, Hugging Face Transformers, scikit-learn (metrics), `garak`, FastAPI (serving),
Docker.

## Scope

One person, 2-3 weekends. A lightweight encoder model (not a full LLM fine-tune), a bounded subset
of Aegis categories (not the full taxonomy), a bounded garak scan (a handful of probe types, not the
full suite). Not a claim of production-grade coverage or large-scale robustness.

## Measured-claim target

Fine-tuned classifier reaches N% F1 on held-out Aegis categories; garak adversarial probing drops
detection rate by M percentage points, identifying which category is most jailbreak-fragile.

## Build spec

1. Download the open Aegis-AI-Content-Safety-Dataset (Hugging Face); select a bounded subset of risk
   categories to scope the classifier.
2. Fine-tune a lightweight transformer encoder (DeBERTa-v3-small or similar) as a multi-label
   classifier over those categories.
3. Evaluate on a held-out split: per-category precision/recall/F1, plus a confusion analysis across
   categories.
4. Run `garak` against the classifier (or an LLM the classifier is meant to guard) using a bounded
   set of jailbreak/adversarial probes; measure the drop in detection rate.
5. Serve the classifier behind a FastAPI endpoint, containerized with Docker, for a reproducible
   demo.
6. Write up the measured claim, including which category was most jailbreak-fragile and why.

## Repo layout

```
src/
  data/       dataset download + preprocessing (Aegis subset selection, label encoding)
  model/      encoder fine-tuning (train.py, model config)
  eval/       held-out metrics + garak adversarial harness
  serve/      FastAPI serving endpoint
tests/        stub tests asserting the shape of each measured claim
scripts/      CLI entry points (train, evaluate, run-garak, serve)
notebooks/    exploratory analysis (confusion matrices, category breakdown)
```

## Status

`queued` → **`scaffolded`** (this commit) → `in-progress` → `built`. See `_Bank/TODO.md` in the JOBS
folder for the canonical spec this was scaffolded from.

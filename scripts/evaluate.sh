#!/usr/bin/env bash
set -euo pipefail
python -c "from src.eval.metrics import evaluate_held_out; print(evaluate_held_out('checkpoints/content-safety-classifier', 'data/processed/test.jsonl'))"

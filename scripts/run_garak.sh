#!/usr/bin/env bash
set -euo pipefail
python -c "from src.eval.adversarial import run_garak_suite; print(run_garak_suite('checkpoints/content-safety-classifier', probe_types=['dan', 'encoding', 'promptinject']))"

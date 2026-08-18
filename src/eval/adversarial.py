"""
Adversarial robustness evaluation using garak (NVIDIA's open-source LLM vulnerability scanner).

TODO (build spec step 4):
    - Wrap the fine-tuned classifier as a garak-compatible "generator"/target.
    - Select a bounded set of jailbreak/adversarial probe types (not the full garak suite).
    - Run garak against the wrapped classifier and record the drop in detection rate vs. the
      clean-set metrics from src/eval/metrics.py.
    - Identify which risk category is most jailbreak-fragile (largest detection-rate drop).
"""

from dataclasses import dataclass


@dataclass
class AdversarialResult:
    probe_name: str
    category: str
    clean_detection_rate: float
    adversarial_detection_rate: float

    @property
    def drop_pp(self) -> float:
        """Percentage-point drop in detection rate under this probe."""
        return (self.clean_detection_rate - self.adversarial_detection_rate) * 100


def run_garak_suite(model_path: str, probe_types: list[str]) -> list[AdversarialResult]:
    """Run a bounded garak probe suite against the classifier and return per-probe results.

    Raises NotImplementedError until build spec step 4 is implemented.
    """
    raise NotImplementedError("garak adversarial harness not yet implemented — see build spec step 4.")


def most_fragile_category(results: list[AdversarialResult]) -> str:
    """Return the category with the largest detection-rate drop under adversarial probing."""
    if not results:
        raise ValueError("No adversarial results to analyze.")
    return max(results, key=lambda r: r.drop_pp).category

"""
Held-out evaluation: per-category precision/recall/F1 and confusion analysis.

TODO (build spec step 3):
    - Run the fine-tuned classifier over the held-out test split.
    - Compute per-category precision, recall, F1 (sklearn.metrics, multi-label aware).
    - Produce a confusion analysis across categories (which categories get mutually confused).
    - Persist results to a structured report (JSON/CSV) for the write-up.
"""

from dataclasses import dataclass


@dataclass
class CategoryMetrics:
    category: str
    precision: float
    recall: float
    f1: float
    support: int


def evaluate_held_out(model_path: str, test_split_path: str) -> list[CategoryMetrics]:
    """Return per-category metrics on the held-out split.

    Raises NotImplementedError until build spec step 3 is implemented.
    """
    raise NotImplementedError("Held-out evaluation not yet implemented — see build spec step 3.")


def confusion_report(model_path: str, test_split_path: str) -> dict:
    """Return a category-by-category confusion breakdown.

    Raises NotImplementedError until build spec step 3 is implemented.
    """
    raise NotImplementedError("Confusion analysis not yet implemented — see build spec step 3.")

"""
Download and preprocess a bounded subset of the Aegis-AI-Content-Safety-Dataset.

TODO (build spec step 1):
    - Load the dataset from Hugging Face (`nvidia/Aegis-AI-Content-Safety-Dataset-1.0` or current
      published id — verify the exact dataset name/version at build time).
    - Select a bounded subset of risk categories (e.g. hate/harassment, sexual, harmful/violent) —
      do not attempt the full taxonomy at this scope.
    - Encode labels as multi-label binary vectors over the selected category subset.
    - Produce a stratified held-out split (train/val/test) with no leakage across splits.
"""

from dataclasses import dataclass
from pathlib import Path


# Bounded subset of Aegis risk categories this project scopes to. Fill in with the
# real category names once the dataset schema has been inspected.
SELECTED_CATEGORIES: list[str] = [
    # "hate_harassment",
    # "sexual",
    # "harmful_violent",
]


@dataclass
class AegisExample:
    text: str
    labels: list[int]  # multi-hot over SELECTED_CATEGORIES


def load_aegis_subset(cache_dir: Path | None = None) -> list[AegisExample]:
    """Load and filter the Aegis dataset down to SELECTED_CATEGORIES.

    Raises NotImplementedError until build spec step 1 is implemented.
    """
    raise NotImplementedError("Aegis dataset loading not yet implemented — see build spec step 1.")


def make_splits(
    examples: list[AegisExample], seed: int = 42
) -> tuple[list[AegisExample], list[AegisExample], list[AegisExample]]:
    """Stratified train/val/test split. Raises NotImplementedError until implemented."""
    raise NotImplementedError("Split logic not yet implemented — see build spec step 1.")

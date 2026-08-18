"""
Fine-tune a lightweight transformer encoder as a multi-label content-safety classifier.

TODO (build spec step 2):
    - Load a lightweight encoder checkpoint (DeBERTa-v3-small or RoBERTa-base).
    - Attach a multi-label classification head sized to len(SELECTED_CATEGORIES).
    - Fine-tune on the Aegis subset train split with a BCE-with-logits loss (multi-label, not
      softmax/single-label).
    - Track validation F1 per category during training for early stopping.
"""

from dataclasses import dataclass
from pathlib import Path


DEFAULT_BASE_MODEL = "microsoft/deberta-v3-small"


@dataclass
class TrainConfig:
    base_model: str = DEFAULT_BASE_MODEL
    max_length: int = 256
    batch_size: int = 16
    learning_rate: float = 2e-5
    num_epochs: int = 3
    seed: int = 42
    output_dir: Path = Path("checkpoints/content-safety-classifier")


def train(config: TrainConfig) -> Path:
    """Fine-tune the classifier and return the path to the saved checkpoint.

    Raises NotImplementedError until build spec step 2 is implemented.
    """
    raise NotImplementedError("Training loop not yet implemented — see build spec step 2.")


if __name__ == "__main__":
    train(TrainConfig())

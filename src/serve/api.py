"""
FastAPI serving endpoint for the fine-tuned content-safety classifier.

TODO (build spec step 5):
    - Load the fine-tuned checkpoint at startup.
    - Expose a POST /classify endpoint accepting text, returning per-category scores + a
      threshold-based flag decision.
    - Containerize with the repo's Dockerfile.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Content-Safety Classifier", version="0.1.0")


class ClassifyRequest(BaseModel):
    text: str


class CategoryScore(BaseModel):
    category: str
    score: float
    flagged: bool


class ClassifyResponse(BaseModel):
    text: str
    scores: list[CategoryScore]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/classify", response_model=ClassifyResponse)
def classify(request: ClassifyRequest) -> ClassifyResponse:
    """Classify text across safety categories.

    Raises NotImplementedError until the model is loaded and build spec step 5 is implemented.
    """
    raise NotImplementedError("Model loading + inference not yet wired up — see build spec step 5.")

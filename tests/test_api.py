"""Stub tests for the serving API."""

import pytest
from fastapi.testclient import TestClient

from src.serve.api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_classify_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        client.post("/classify", json={"text": "sample input"})


# TODO once implemented:
# - assert /classify returns a score per SELECTED_CATEGORIES
# - assert flagged=True triggers correctly above the chosen threshold
# - measure and assert p95 latency for a bounded prompt length, per serving demo goal

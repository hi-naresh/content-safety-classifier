"""Stub tests for evaluation modules — encode the measured-claim target as assertions to fill in."""

import pytest

from src.eval.metrics import evaluate_held_out, confusion_report
from src.eval.adversarial import (
    AdversarialResult,
    run_garak_suite,
    most_fragile_category,
)


def test_evaluate_held_out_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        evaluate_held_out("dummy-model", "dummy-split")


def test_confusion_report_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        confusion_report("dummy-model", "dummy-split")


def test_run_garak_suite_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        run_garak_suite("dummy-model", probe_types=["dan", "encoding"])


def test_most_fragile_category_picks_largest_drop():
    """This one IS implemented (pure logic, no model needed) — sanity-checks the helper itself."""
    results = [
        AdversarialResult("probe_a", "hate_harassment", clean_detection_rate=0.90, adversarial_detection_rate=0.85),
        AdversarialResult("probe_b", "sexual", clean_detection_rate=0.92, adversarial_detection_rate=0.60),
        AdversarialResult("probe_c", "harmful_violent", clean_detection_rate=0.88, adversarial_detection_rate=0.80),
    ]
    assert most_fragile_category(results) == "sexual"


def test_most_fragile_category_empty_raises():
    with pytest.raises(ValueError):
        most_fragile_category([])


# TODO once evaluate_held_out is implemented, add the real measured-claim assertions, e.g.:
# def test_f1_meets_target_threshold():
#     metrics = evaluate_held_out(TRAINED_MODEL_PATH, TEST_SPLIT_PATH)
#     assert all(m.f1 > 0.0 for m in metrics)  # replace 0.0 with the actual target once measured
#
# def test_garak_drop_is_reported_not_asserted_blind():
#     results = run_garak_suite(TRAINED_MODEL_PATH, probe_types=[...])
#     assert len(results) > 0
#     assert most_fragile_category(results) in KNOWN_CATEGORIES

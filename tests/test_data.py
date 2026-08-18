"""Stub tests for the data loading module. Fill in once src/data/aegis.py is implemented."""

import pytest

from src.data.aegis import load_aegis_subset, make_splits, SELECTED_CATEGORIES


def test_selected_categories_nonempty_once_scoped():
    """SELECTED_CATEGORIES should be filled in with a bounded subset before build starts."""
    # Currently empty by design (scaffold state) — flip this assertion once categories are chosen.
    assert isinstance(SELECTED_CATEGORIES, list)


def test_load_aegis_subset_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        load_aegis_subset()


def test_make_splits_not_yet_implemented():
    with pytest.raises(NotImplementedError):
        make_splits([])


# TODO once implemented:
# - assert no example appears in more than one of train/val/test (leakage check)
# - assert every example's label vector has length == len(SELECTED_CATEGORIES)
# - assert split proportions are roughly as configured

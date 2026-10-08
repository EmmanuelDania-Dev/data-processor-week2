import pytest

from transformations import (
    filter_rows,
    is_engineer,
    get_engineers,
    filter_by_department,
)


def test_filter_rows():
    rows = [
        {"name": "Ada", "department": "Engineering"},
        {"name": "John", "department": "Sales"},
        {"name": "Grace", "department": "Engineering"},
    ]

    result = list(
        filter_rows(
            rows,
            lambda row: row["department"] == "Engineering"
        )
    )

    assert len(result) == 2
    assert result[0]["name"] == "Ada"
    assert result[1]["name"] == "Grace"


def test_is_engineer():
    row = {
        "name": "Ada",
        "department": "Engineering"
    }

    assert is_engineer(row) is True


def test_is_engineer_returns_false_for_other_department():
    row = {
        "name": "John",
        "department": "Sales"
    }

    assert is_engineer(row) is False


def test_is_engineer_missing_department():
    row = {
        "name": "Ada"
    }

    with pytest.raises(
        KeyError,
        match="Missing required column"
    ):
        is_engineer(row)


def test_get_engineers():
    rows = [
        {"name": "Ada", "department": "Engineering"},
        {"name": "John", "department": "Sales"},
        {"name": "Grace", "department": "Engineering"},
    ]

    result = list(get_engineers(rows))

    assert len(result) == 2
    assert all(
        row["department"] == "Engineering"
        for row in result
    )


def test_filter_by_department():
    rows = [
        {"name": "Ada", "department": "Engineering"},
        {"name": "John", "department": "Sales"},
        {"name": "Grace", "department": "Engineering"},
    ]

    result = list(
        filter_by_department(rows, "Sales")
    )

    assert len(result) == 1
    assert result[0]["name"] == "John"


def test_filter_by_department_empty_department():
    rows = []

    with pytest.raises(
        ValueError,
        match="Department cannot be empty"
    ):
        filter_by_department(rows, "")

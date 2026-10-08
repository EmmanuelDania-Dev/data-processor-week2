import json

import pytest

from processor import CSVProcessor


def test_read_rows(tmp_path):
    file_path = tmp_path / "employees.csv"

    file_path.write_text(
        "id,name,department\n"
        "1,Ada,Engineering\n"
        "2,John,Sales\n"
    )

    processor = CSVProcessor(str(file_path))

    rows = list(processor.read_rows())

    assert len(rows) == 2
    assert rows[0]["name"] == "Ada"
    assert rows[1]["department"] == "Sales"


def test_read_all_rows(tmp_path):
    file_path = tmp_path / "employees.csv"

    file_path.write_text(
        "id,name,department\n"
        "1,Ada,Engineering\n"
        "2,John,Sales\n"
    )

    processor = CSVProcessor(str(file_path))

    rows = processor.read_all_rows()

    assert len(rows) == 2


def test_read_rows_without_header(tmp_path):
    file_path = tmp_path / "employees.csv"

    file_path.write_text("")

    processor = CSVProcessor(str(file_path))

    with pytest.raises(
        ValueError,
        match="CSV file has no header"
    ):
        list(processor.read_rows())


def test_to_json():
    processor = CSVProcessor("employees.csv")

    rows = [
        {
            "name": "Ada",
            "department": "Engineering"
        }
    ]

    result = processor.to_json(rows)

    parsed_result = json.loads(result)

    assert parsed_result == rows


def test_to_json_empty_rows():
    processor = CSVProcessor("employees.csv")

    result = processor.to_json([])

    assert json.loads(result) == []


def test_empty_filename():
    with pytest.raises(
        ValueError,
        match="Filename cannot be empty"
    ):
        CSVProcessor("")

import pytest

from context_manager import CSVFile


def test_csv_file_opens_and_closes(tmp_path):
    file_path = tmp_path / "test.csv"

    file_path.write_text(
        "name,department\n"
        "Ada,Engineering\n"
    )

    with CSVFile(file_path) as file:
        assert not file.closed

        content = file.read()

        assert content.replace("\r\n", "\n") == (
            "name,department\n"
            "Ada,Engineering\n"
        )

    assert file.closed


def test_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        with CSVFile("does_not_exist.csv"):
            pass


def test_csv_file_permission_error(monkeypatch):
    def mock_open(*args, **kwargs):
        raise PermissionError("Access denied")

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(
        PermissionError,
        match="Permission denied"
    ):
        with CSVFile("employees.csv"):
            pass

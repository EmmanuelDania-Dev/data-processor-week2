import csv
import json
from collections.abc import Iterable, Iterator

from context_manager import CSVFile
from decorators import process_log


Row = dict[str, str]


class CSVProcessor:
    def __init__(self, filename: str) -> None:
        if not filename:
            raise ValueError("Filename cannot be empty.")

        self.filename: str = filename

    def read_rows(self) -> Iterator[Row]:
        try:
            with CSVFile(self.filename) as file:
                reader = csv.DictReader(file)

                if reader.fieldnames is None:
                    raise ValueError(
                        f"CSV file has no header: {self.filename}"
                    )

                for row in reader:
                    yield row

        except csv.Error as error:
            raise ValueError(
                f"Invalid CSV data in '{self.filename}': {error}"
            ) from error

    def read_all_rows(self) -> list[Row]:
        return list(self.read_rows())

    @process_log
    def to_json(self, rows: Iterable[Row]) -> str:
        try:
            return json.dumps(
                list(rows),
                indent=4
            )

        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Could not convert rows to JSON: {error}"
            ) from error

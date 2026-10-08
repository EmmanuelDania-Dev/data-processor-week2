from typing import Optional, TextIO


class CSVFile:
    """Context manager for safely opening and closing a CSV file."""

    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.file: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        try:
            self.file = open(
                self.filename,
                "r",
                newline="",
                encoding="utf-8"
            )
            return self.file

        except FileNotFoundError:
            raise FileNotFoundError(
                f"CSV file not found: {self.filename}"
            )

        except PermissionError:
            raise PermissionError(
                f"Permission denied when opening: {self.filename}"
            )

        except OSError as error:
            raise OSError(
                f"Could not open file '{self.filename}': {error}"
            ) from error

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object
    ) -> bool:
        if self.file is not None:
            self.file.close()

        return False

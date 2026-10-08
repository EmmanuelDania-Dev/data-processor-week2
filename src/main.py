from processor import CSVProcessor
from transformations import get_engineers


def main() -> None:
    try:
        processor = CSVProcessor("employees.csv")

        rows = processor.read_rows()
        engineers = get_engineers(rows)

        result = processor.to_json(engineers)

        print(result)

    except FileNotFoundError as error:
        print(f"File error: {error}")

    except PermissionError as error:
        print(f"Permission error: {error}")

    except ValueError as error:
        print(f"Data error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

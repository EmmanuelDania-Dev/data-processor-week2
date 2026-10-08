# Data Processor — FIP Internship Week 2

A Python-based CSV data processing project

The project demonstrates practical Python concepts including context managers, data transformations, decorators, error handling, type hints, and automated testing with pytest.

## Project Overview

The goal of this project is to build a simple and maintainable data processing pipeline that can:

- Read data from a CSV file.
- Safely manage file resources using a custom context manager.
- Transform and filter CSV data.
- Filter employees by department.
- Convert processed data to JSON.
- Log processing operations using a decorator.
- Handle common file and data errors.
- Use type hints throughout the codebase.
- Test the application's components using pytest.

## Project Structure

```text
data-processor/
│
├── .gitignore
├── README.md
│
└── src/
    ├── context_manager.py
    ├── decorators.py
    ├── employees.csv
    ├── main.py
    ├── processor.py
    ├── transformations.py
    │
    └── tests/
        ├── test_context_manager.py
        ├── test_processor.py
        └── test_transformations.py

## Technologies Used

- Python 3

- CSV module

- JSON module

- Pytest

- Git & GitHub

## Key Concepts Demonstrated
**Context Managers**

A custom CSVFile context manager is used to safely open and close CSV files.

with CSVFile(self.filename) as file:
    ...


This ensures that the file is properly closed after processing, including when an exception occurs.

**Data Transformations**

The project includes reusable transformations for filtering rows and selecting employees by department.

For example:

engineers = get_engineers(rows)

**Decorators**

A process_log decorator is used to log the start, successful completion, and failure of processing operations.

**Error Handling**

The project handles errors such as:

- Missing files

- Permission errors

- Invalid CSV data

- Missing CSV columns

- Invalid input values

- JSON conversion errors

**Type Hints**

Type hints are used throughout the project to make the code easier to understand and maintain.

Example:

def read_all_rows(self) -> list[Row]:
    ...

**Testing**

The project uses pytest to test:

- File opening and closing

- Missing files

- Permission errors

- CSV processing

- JSON conversion

- Data filtering

- Missing columns

- Invalid input

All tests currently pass successfully.

## How to Run the Project
1. Clone the repository
git clone <https://github.com/EmmanuelDania-Dev/data-processor-week2.git>
cd data processor

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment

On Windows:

.venv\Scripts\Activate.ps1


On macOS/Linux:

source .venv/bin/activate

4. Install pytest
python -m pip install pytest

5. Run the application

Move into the src directory:

cd src


Then run:

python main.py


The processor reads employees.csv, filters the Engineering employees, and outputs the resulting records as JSON.

Running the Tests

From the src directory:

pytest


**Expected result:**

16 passed

## Demo

A short recording demonstrating the project running successfully is available here:

**Demo Recording:**
https://drive.google.com/file/d/1WUmdZ0MjV1giDdamKozNvRKqq_mxWJOg/view?usp=sharing

Internship

This project was completed as part of my Week 2 assignment for the FIP Internship.

The assignment provided an opportunity to practice writing modular Python code, implementing context managers, handling errors, applying type hints, and writing automated tests.

## Author

Dania Emmanuel
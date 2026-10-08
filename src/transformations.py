def filter_rows(rows, condition):
    """
    Return only rows that satisfy the given condition.
    """
    for row in rows:
        try:
            if condition(row):
                yield row

        except (KeyError, TypeError) as error:
            raise ValueError(
                f"Invalid row data: {row}"
            ) from error


def is_engineer(row):
    """
    Check whether an employee belongs to Engineering.
    """
    if "department" not in row:
        raise KeyError(
            "Missing required column: 'department'"
        )

    return row["department"] == "Engineering"


def get_engineers(rows):
    """
    Return only employees from the Engineering department.
    """
    return filter_rows(rows, is_engineer)


def filter_by_department(rows, department):
    """
    Return rows belonging to the specified department.
    """
    if not department:
        raise ValueError(
            "Department cannot be empty."
        )

    return filter_rows(
        rows,
        lambda row: row["department"] == department
    )

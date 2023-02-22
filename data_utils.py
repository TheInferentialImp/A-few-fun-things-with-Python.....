"""Dictionary related utility functions."""

__author__ = "730622857"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str]  of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Visualizing only a few rows of a table with an overwhelming amount of information."""
    result: dict[str, list[str]] = {}
    for column_header in column_table:
        if rows >= len(column_table[column_header]):
            return column_table
        new_list: list[str] = []
        i: int = 0
        while i < rows:
            new_list.append(column_table[column_header][i])
            i += 1
        result[column_header] = new_list
    return result


def select(column_table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Used for selecting desirable columns."""
    result: dict[str, list[str]] = {}
    for column in column_name:
        result[column] = column_table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine data from different sources."""
    result: dict[str, list[str]] = {}
    for line_1 in table_1:
        result[line_1] = table_1[line_1]
    for line_2 in table_2:
        if line_2 in result:
            result[line_2] += table_2[line_2]
        else:
            result[line_2] = table_2[line_2]
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Count the number of times a unique value appeared in the input list."""
    result: dict[str, int] = {}
    for line in given_list:
        if line in result:
            result[line] += 1
        else:
            result[line] = 1
    return result
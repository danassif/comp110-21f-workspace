"""Utility functions."""

__author__ = "123456789"

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return a column's values."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert a table of rows to a table of columns."""
    result: dict[str, list[str]] = {}
    for key in table[0]:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """done."""
    result: dict[str, list[str]] = {}
    if N < len(table):
        for col in table:
            i: int = 0
            empty_list: list[str] = []
            while i < N:
                empty_list.append(table[col][i])
                i += 1
            result[col] = empty_list
        return result
    else:
        return table


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Select only a subset of columns."""
    result: dict[str, list[str]] = {}
    for col in cols:
        result[col] = table[col]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat two dicts."""
    result: dict[str, list[str]] = {}
    for col in table1:
        result[col] = table1[col]
    
    for col in table2:
        if col in result:
            result[col] += table2[col]
        else:
            result[col] = table2[col]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Get counts of each value."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

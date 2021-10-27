"""List utility functions part 2."""

__author__ = "123456789"

"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def only_evens(given: list[int]) -> list[int]:
    """Function that returns only the evens."""
    empty: list[int] = []
    i: int = 0
    while i < len(given):
        if given[i] % 2 == 0:
            empty.append(given[i])
        i += 1
    return empty


def sub(given: list[int], start: int, end: int) -> list[int]:
    """Function that returns a subset of the list we gave it."""
    empty: list[int] = []
    if len(given) == 0 or start > len(given) or end <= 0:
        return empty
    if start < 0:
        start = 0
    if end > len(given):
        end = len(given)
    i: int = start
    sub: list[int] = []
    while i < end:
        sub.append(given[i])
        i += 1
    return sub


def concat(a: list[int], b: list[int]) -> list[int]:
    """A function that concatenates two lists."""
    new: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(a):
        new.append(a[i])
        i += 1
    while j < len(b):
        new.append(b[j])
        j += 1
    return new

"""List utility functions."""

__author__ = "David"


def max(x: list[int]) -> int:
    """Find maximum value."""
    if len(x) == 0:
        raise ValueError("max() arg is empty")
    else:
        initial: int = x[0]
        i: int = 1
        while i < len(x):
            if x[i] > initial:
                initial = x[i]
            i += 1
        return initial


def all(x: list[int], y: int) -> bool:
    """Return True if all elements in a list are equal."""
    if len(x) == 0:
        return False

    i: int = 0
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Compare equality of two lists."""
    if len(x) != len(y):
        return False
    
    i: int = 0
    while i < len(x):
        if x[i] != y[i]:
            return False
        i += 1
    return True
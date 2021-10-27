"""Practice with dictionaries."""

__author__ = "123456789"
"""Practice with dictionaries."""


def count(values: list[str]) -> dict[str, int]:
    """Get counts of each value."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def invert(param: dict[str, str]) -> dict[str, str]:
    """Inverting a dictionary."""
    out: dict[str, str] = {}
    for key in param:
        value = param[key]
        if value in out:
            raise KeyError("Non Unique Keys!")
        else:
            out[value] = key
    return out


def favorite_color(students: dict[str, str]) -> str:
    """Return the most common favorite color."""
    color_counts: dict[str, int] = {}
    for student in students:
        if students[student] in color_counts.keys():
            color_counts[students[student]] += 1
        else:
            color_counts[students[student]] = 1 
    winning_color: str = ""
    max: int = 0 
    for color in color_counts:
        if color_counts[color] > max:
            max = color_counts[color]
            winning_color = color 
    return winning_color
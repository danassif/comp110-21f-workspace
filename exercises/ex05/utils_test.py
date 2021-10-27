from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_negnums() -> None:
    """Test only_evens."""
    assert only_evens([-1, -2, -3, -4]) == [-2, -4]


def test_only_evens_emptylist() -> None:
    """Test only_evens."""
    assert only_evens([]) == []


def test_only_evens_odds() -> None:
    """Test only_evens."""
    assert only_evens([1, 3, 5]) == []


def test_sub_test_negnums() -> None:
    """Test sub."""
    assert sub([-1, -2, -3, -4], 1, 3) == [-2, -3]


def test_sub_test_emptylist() -> None:
    """Test sub."""
    assert sub([], 1, 4) == []


def test_sub_test_badindex() -> None:
    """Test sub."""
    assert sub([1, 2, 3, 4], 2, 1) == []


def test_concat_test_normal() -> None:
    """Test of concat."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_test_negnums() -> None:
    """Test of concat."""
    assert concat([-1, -2, -3], [-4]) == [-1, -2, -3, -4]


def test_concat_test_emptylist() -> None:
    """Test of concat."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]    
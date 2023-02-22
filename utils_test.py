"""Unit tests for utils."""

__author__ = "730622857"


from utils import only_evens
from utils import concat
from utils import sub


def test_only_evens_empty() -> None: 
    """Function test given an empty parameter."""
    given_list: list[int] = []
    assert only_evens(given_list) == []


def test_only_evens_single_item() -> None: 
    """Function test given only a single item."""
    given_list: list[int] = [2]
    assert only_evens(given_list) == [2]


def test_only_even_negative() -> None: 
    """Function test given a parameter with negative integers."""
    given_list: list[int] = [-1, -2, -3]
    assert only_evens(given_list) == [-2]


def test_concat_empty() -> None:
    """Function test given an empty parameter."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == ([])


def test_concat_single_list() -> None:
    """Function test given only a single parameter."""
    x: list[int] = [1, 2, 3]
    y: list[int] = []
    assert concat(x, y) == [1, 2, 3]


def test_concat_negative() -> None:
    """Function test given a expected x paramater and a y parameter containing negative integers."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [-1, -2, - 3]
    assert concat(x, y) == ([1, 2, 3, -1, -2, -3])

    
def test_sub_list_no_startstop() -> None:
    """Function test given a list but no start/stop parameters."""
    given_list: list[int] = [10, 20, 30, 40]
    start: int = ()
    stop: int = ()
    assert sub(given_list, start, stop) == ([])


def test_sub_empty_list_and_parameters() -> None:
    """Function test given no list or parameters."""
    given_list: list[int] = []
    start: int = ()
    stop: int = ()
    assert sub(given_list, start, stop) == ([])


def test_sub_list_with_negative_start() -> None:
    """Function test given a list with a negative start."""
    given_list: list[int] = [10, 20, 30, 40]
    start: int = (-2)
    stop: int = (3)
    assert sub(given_list, start, stop) == [10, 20, 30]
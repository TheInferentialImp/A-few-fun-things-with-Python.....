"""Test functions in exercises.dictionary."""

__author__ = "730622857"

from dictionary import favorite_color
from dictionary import invert
from dictionary import count
import pytest


def test_favorite_color_empty() -> None:
    """Empty params."""
    given_dict: dict[str, str] = {}
    assert favorite_color(given_dict) == pytest.raises(ValueError)


def test_favorite_color_single_item() -> None:
    """Single param."""
    given_dict: dict[str, str] = {"alex": "red"}
    assert favorite_color(given_dict) == "red"


def test_favorite_color_many_items() -> None:
    """Usual test case."""
    given_dict: dict[str, str] = {"alex": "red", "davis": "blue", "kris": "green", "david": "blue", "jerry": "green", "john": "blue"}
    assert favorite_color(given_dict) == "blue"


def test_count_empty() -> None:
    """Empty params."""
    given_list: list[str] = []
    assert count(given_list) == {}


def test_count_singe_item() -> None:
    """Single param."""
    given_list: list[str] = ["alex"]
    assert count(given_list) == {"alex": 1}


def test_count_many_items() -> None:
    """Usual test case."""
    given_list: list[str] = ["alex", "kris", "kris", "alex", "david"]
    assert count(given_list) == {"alex": 2, "kris": 2, "david": 1}


def test_invert_empty() -> None:
    """Empty params."""
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == {}


def test_invert_single_item() -> None:
    """Single param."""
    given_dict: dict[str, str] = {"x", "y"}
    assert invert(given_dict) == {"y", "x"}


def test_invert_many_items() -> None:
    """Usual test case."""
    given_dict: dict[str, str] = {"alex": "kris", "kris": "alex", "kylie": "david"}
    assert invert(given_dict) == {"kris": "alex", "alex": "kris", "david": "kylie"}
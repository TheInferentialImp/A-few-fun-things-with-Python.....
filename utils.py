"""Util functions created for unit tests."""

__author__ = "730622857"


def only_evens(given_list: list[int]) -> list: 
    """Given a list, this function returns only even numbers."""
    evens: list = []
    odds: list = []
    for i in given_list: 
        if (i % 2 == 0): 
            evens.append(i)
        else:
            odds.append(i)
    return evens


def concat(x: list[int], y: list[int]) -> list[int]: 
    """Given two lists, this function produces one list of paramater x followed by list of parameter y."""
    new_list: list[int] = []
    i: int = 0
    while i < len(x):
        new_list.append(x[i])
        i += 1
    b: int = 0
    while b < len(y):
        new_list.append(y[b])
        b += 1
    return new_list


def sub(given_list: list[int], start: int, stop: int) -> list: 
    """Given a list in addition to a start and stop index, sub will trim the list between from start to the stop."""
    new_list: list = []
    i: int = start
    if start == (): 
        if stop == (): 
            return [] 
    if start < 0: 
        i = 0
    if stop > len(given_list): 
        stop = len(given_list)
    if len(given_list) == 0: 
        return []
    if start >= len(given_list): 
        return []
    if stop < 0: 
        return []
    while i < stop: 
        new_list.append(given_list[i])
        i += 1
    return new_list
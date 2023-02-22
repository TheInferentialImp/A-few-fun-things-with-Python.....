"""EXO4 - Utils: displays utlities of lists in Python."""

__author__ = "730622857"

def all(x: list[int], y:int) -> bool:
    """Given a list of ints and an int, indicates whether or not they are all identical to the given int."""
    if x == []:
        return False
    if y == ():
        return False
    i: int = 0
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True
def __repr__(self) -> str:
        new_string: str=  repr(self.values)
        return f"Simpy({new_string})"
def max(x: list[int]) -> int:
    """Use this to return the largest value given a list of ints."""
    i: int = 1
    max: int = x[0]  #  use x[0] instead of just a i counter
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(x):
        if x[i] > max:
            max = x[i]  #  reassigns max to with new found maximum
        i += 1
    return max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Use this to determine if a given list is identical to another list."""
    if x != y:  #  ends function and returns False if lists !=
        return False
    else:
        return True



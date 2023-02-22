"""Functions utilizing dictionaries."""

__author__ = "730622857"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionaries key:value pairs."""
    inverted_dict: dict = {}
    for column in given_dict:
        value = given_dict[column]
        if value in inverted_dict:
            raise KeyError("Keys must not be identical.")
        inverted_dict[value] = column
    return inverted_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Select the most common color in a dictionary given name:color pairs."""
    i: int = 0
    diction: dict[str, int] = {}
    diction_2: dict[str, int] = {}
    if given_dict == {}:
        raise ValueError("Your dictionary must have multiple (3+) key:value pairs")
    for name in given_dict:
        color = given_dict[name]
        if color in diction:
            diction[color] += 1
        else:
            diction[color] = 1
            diction_2[color] = i
        i += 1
    max: int = 0
    final_color: str = ""
    for color in diction:
        if diction[color] > max:
            max = diction[color]
            final_color = color
        elif max == diction[color]:
            if diction_2[final_color] > diction_2[color]:
                final_color = color
    return final_color


def count(given_list: list[str]) -> dict[str, int]:
    """Given a string, count returns the instances of each character in a dict as the string being the key and instances of the string in the list as the value."""
    freq_dict: dict[str, int] = {}
    for item in given_list:            
        if item in freq_dict:      
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
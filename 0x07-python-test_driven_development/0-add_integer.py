#!/usr/bin/python3
"""

Module add-integer
adds two integer
"""
def add_integer(a, b=98):
    """
    return the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

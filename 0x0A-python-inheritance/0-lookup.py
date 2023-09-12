#!/usr/bin/python3

"""module contains lookup function"""


def lookup(obj):
    """
    returns the list of available attributes
    and methods of an object.

    Args:
        obj: object to print..

    Return:
        list of all attributes and methods.
    """
    return dir(obj)

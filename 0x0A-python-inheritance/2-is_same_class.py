#!/usr/bin/python3

"""module contains function """


def is_same_class(obj, a_class):
    """
    function that return True ifthe object is exactly an
    instance of the specified class ; otherwise False.

    Args:
        obj: object
        a_class: class

    Retuen:
        boolean value
    """
    return type(obj) is a_class

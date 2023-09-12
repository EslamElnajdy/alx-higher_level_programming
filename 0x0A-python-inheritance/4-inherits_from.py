#!/usr/bin/python3

"""module contains function """


def inherits_from(obj, a_class):
    """
    function doc
    """
    return isinstance(obj, a_class) and type(obj) != a_class

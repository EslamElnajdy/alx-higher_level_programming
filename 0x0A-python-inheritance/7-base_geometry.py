#!/usr/bin/python3

""" module doc"""


class BaseGeometry:
    """
    class doc
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates the integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

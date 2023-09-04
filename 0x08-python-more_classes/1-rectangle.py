#!/usr/bin/python3
"""
class module
"""


class Rectangle:
    """
    Rectangle class
    """

    @property
    def width(self):
        """
        get the attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """
        initialize the attributes

        Args:
            width: number of width
            height: number of width
        """
        self.__width = width
        self.__height = height

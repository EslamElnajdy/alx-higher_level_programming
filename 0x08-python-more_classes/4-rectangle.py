#!/usr/bin/python3
"""
class module
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        initialize the attributes

        Args:
            width: number of width
            height: number of width
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """
        print the rectangle with the character #
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            rec_str += "#" * self.__width + '\n'
        return rec_str[:-1]

    def __repr__(self) -> str:
        """
        return a string representation of the rectangle to
        be able to recreate a new instance by using eval()
        """
        return("Rectangle({}, {})".format(self.__width, self.__height))

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

    def area(self):
        """
        Return the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

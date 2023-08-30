#!/usr/bin/python3
""" Square module """


class Square:
    """ body of  a square class """

    def __init__(self, size=0) -> None:
        """
        Initializes class attributes

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """
        get the attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size ** 2

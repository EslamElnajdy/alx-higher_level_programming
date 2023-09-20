#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def check(self, target, name_target):
        """validation of all setter methods"""

        if not isinstance(target, int):
            raise TypeError(f"{name_target} must be an integer")
        if name_target == "x" or name_target == "y":
            if target < 0:
                raise ValueError(f"{name_target} must be >= 0")
        else:
            if target <= 0:
                raise ValueError(f"{name_target} must be > 0")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.check(width, "width")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.check(height, "height")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.check(x, "x")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.check(y, "y")
        self.__y = y

    def area(self):
        """Return the area of reactangle"""

        return self.__height * self.__width

    def display(self):
        """print # according to area"""
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end='')
            print()

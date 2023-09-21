#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class -> Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            size: size of square
            x: position of square
            y: position of square
            id: id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriden __str__
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        lst = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                args + lst[len(args):len(lst)]
        if kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

#!/usr/bin/python3
"""writing a base geometry class"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherit from base geometry"""

    def __init__(self, width, height):
        """a constructor class for rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

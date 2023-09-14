#!/usr/bin/python3
"""
Module for class Student.
"""


class Student:
    """
    A class students that defines a student by:
    Attributes:
        first_name (str): name of student.
        last_name (str): name of student.
        age (int): age of student.
    """

    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of Student.
        """
        return self.__dict__
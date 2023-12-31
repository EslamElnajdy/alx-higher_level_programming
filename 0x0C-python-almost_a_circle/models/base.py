#!/usr/bin/python3
""" base module"""
import json
import os


class Base:
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - initialization
        Args:
            id: param id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            lst = "[]"
        else:
            lst = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(filename, "w") as f:
            f.write(lst)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances ...
        """
        filename = cls.__name__ + ".json"
        lst = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                s = file.read()
                list_dict = cls.from_json_string(s)
                for d in list_dict:
                    lst.append(cls.create(**d))
        return lst

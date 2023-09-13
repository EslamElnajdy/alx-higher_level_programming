#!/usr/bin/python3
"""module doc"""
import json


def save_to_json_file(my_obj, filename):
    """
    func doc
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))

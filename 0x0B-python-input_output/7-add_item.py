#!/usr/bin/python3
"""module doc"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    func doc
    """
    filename = "add_item.json"
    if path.isfile(filename):
        f_list = load_from_json_file(filename)
    else:
        f_list = []
    for i in range(1, len(argv)):
        f_list.append(sys.argv[i])
    save_to_json_file(f_list, filename)


add_items()

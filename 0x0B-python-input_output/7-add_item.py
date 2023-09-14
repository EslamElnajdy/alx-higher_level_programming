#!/usr/bin/python3
"""Module doc"""
import json
import os.path
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
j_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for index in argv[1:]:
    j_list.append(index)

save_to_json_file(j_list, filename)

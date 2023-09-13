#!/usr/bin/python3
"""module doc"""


def read_file(filename=""):
    """
    func doc
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")

#!/usr/bin/python3
"""module doc"""


def write_file(filename="", text=""):
    """
    func doc
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count

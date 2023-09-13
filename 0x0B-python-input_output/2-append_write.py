#!/usr/bin/python3
"""module doc"""


def append_write(filename="", text=""):
    """
    func doc
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count

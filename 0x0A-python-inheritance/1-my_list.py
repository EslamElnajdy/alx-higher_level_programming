#!/usr/bin/python3

"""module contains a class MyList"""


class MyList(list):
    """
    class that inherits from list
    """

    def print_sorted(self):
        """
        method that print the list, but sorted.
        """
        sorted_l = super().copy()
        sorted_l.sort()
        print(sorted_l)

#!/usr/bin/python3
"""script to return the peak value
"""


def find_peak(list_of_integers):
    """ return the peak value"""
    if not list_of_integers:
        return None

    sorted_list = sorted(list_of_integers)
    return sorted_list[-1]

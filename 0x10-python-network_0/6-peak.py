#!/usr/bin/python3
"""script to return the peak value
"""


def find_peak(list_of_integers):
    """ return the peak value"""
    peak = None
    for ele in list_of_integers:
        if peak is None or peak < ele:
            peak = ele
    return peak

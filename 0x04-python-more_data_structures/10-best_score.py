#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = (0, "")
    for key in a_dictionary:
        if a_dictionary[key] > value[0]:
            value = (a_dictionary[key], key)
    return value[1]

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()
    for i in set_1:
        if i in set_2:
            continue
        else:
            diff_set.add(i)
    for i in set_2:
        if i in set_1:
            continue
        else:
            diff_set.add(i)
    return diff_set

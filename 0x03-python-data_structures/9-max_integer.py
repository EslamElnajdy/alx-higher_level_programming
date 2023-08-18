#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_ele = my_list[0]
    for i in my_list:
        if i > max_ele:
            max_ele = i
    return max_ele

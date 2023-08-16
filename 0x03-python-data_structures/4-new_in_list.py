#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    a = []
    if idx >= 0 and idx < len(my_list):
        a = my_list[:idx] + [element] + my_list[idx + 1:]
    return (a)

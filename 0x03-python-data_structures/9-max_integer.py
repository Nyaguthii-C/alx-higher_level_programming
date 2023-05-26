#!/usr/bin/python3
"""
a function that finds the biggest integer of a list
"""


def max_integer(my_list=[]):
    i = 0
    if len(my_list) == 0:
        return None
    else:
        my_list = sorted(my_list)
    return my_list[-1]

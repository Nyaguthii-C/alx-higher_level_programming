#!/usr/bin/python3
"""
a function that finds all multiples of 2 in a list
"""


def divisible_by_2(my_list=[]):
    new_list = []

    for i in range(0, len(my_list)):
        x = my_list[i]

        if x % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

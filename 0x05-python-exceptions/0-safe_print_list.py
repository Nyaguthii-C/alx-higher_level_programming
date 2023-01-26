#!/usr/bin/python3
"""
prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    """
    Args:
        my_list[] - list of elements to be printed
        x - number of elements to be printed
    Returns:
        real number of elements printed
    """
    elems = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elems += 1
        except IndexError:
            break
    print("")
    return elems

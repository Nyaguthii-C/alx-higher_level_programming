#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Args:
        my_list[] - list of elements to be printed
        x - number of ele,ents to print
    Returns:
        - integers in the list
        elems - number of integers printed
    """
    elems = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elems += 1
        except (TypeError, ValueError):
            continue
    print("")
    return elems

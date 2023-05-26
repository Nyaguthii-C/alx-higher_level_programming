#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Args:
        my_list[] - list
        idx: the index of the list item to be deleted
    Returns:
        list if idx is negative or greater than lenght of list
        else, deletes item in idx position and returns list

    """
    if 0 <= idx <= len(my_list):
        del(my_list[idx])
    return my_list

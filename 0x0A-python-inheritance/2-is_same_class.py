#!/usr/bin/python3
"""
a function that returns True
if the object is exactly an instance of the specified class ;
otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args: obj - object to chect type
         a_class - class whose instance is compared to obj
    Return: True if obj is exactly an instance of a_class, else False
    """
    if type(obj) == a_class:
        return True
    else:
        return False

#!/usr/bin/python3
def safe_print_integer(value):
    """
    Args:
        value - interger to be printed
    Returns:
        True - if value is printed correctly
        False - otherwise.
    ValueError added to exception to allow printing str wirh :d
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

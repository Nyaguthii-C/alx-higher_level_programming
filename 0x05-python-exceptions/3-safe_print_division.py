#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Args:
     - a, b - integers to be divided
    returns:
        value after division
    """
    try:
        x = a/b
    except (ZeroDivisionError, ValueError):
        x = None
    finally:
        print("Inside result:{}".format(x))
    return x

#!//usr/bin/python3
"""
 a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
        a: integer or to be added
        b: integer or to be added
    Returns:
        an integer: the addition of a and b
        or raises TypeError if args not int or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a+b)

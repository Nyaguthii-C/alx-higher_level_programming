#!/usr/bin/python3
"""
a function that checks for lowercase character
"""


def islower(c):
    if (ord(c) >= 97) and (ord(c) <= 122):
        return True
    else:
        return False

#!/usr/bin/python3
"""Defines a function that sorts and prints a list"""


class MyList(list):
    """class inheriting list"""
    def print_sorted(self):
        """sort and print inherited list"""
        print(sorted(self))

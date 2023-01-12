#!/usr/bin/python3
"""
writes string to text file (UTF8)
and returns number of characters written
"""


def write_file(filename="", text=""):
    """ open file in the write mode and return written content """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

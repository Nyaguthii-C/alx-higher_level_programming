#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ opens the file encoded with utf-8 and prints content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

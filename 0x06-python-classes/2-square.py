#!/usr/bin/python3
""" A class Square with private instance attribute size """


class Square:
    """ define a the size of the square """
    def __init__(self, size=0):
        """ Instantiation of size """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

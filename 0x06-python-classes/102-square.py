#!/usr/bin/python3
"""
A class Square with private instance attribute size
and a public instance method area
Square instance can answer to comparators:
==, !=, >, >=, < and <= based on the square area
"""


class Square:
    """ define a the size of the square """
    def __init__(self, size=0):
        """ Instantiation of size """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """retrieves size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

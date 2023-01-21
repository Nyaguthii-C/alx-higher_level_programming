#!/usr/bin/python3
"""
A class Square with private instance attribute size
and a public instance method area
and property setter for private attribut size
with a public instance method that prints square with #
"""


class Square:
    """ define a the size of the square """
    def __init__(self, size=0):
        """ Instantiation of size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

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

    def my_print(self):
        """ prints in stdout square with # """
        if self.__size == 0:
            print("\n")
        for i in range(self.__size):
            print('#' * self.__size)

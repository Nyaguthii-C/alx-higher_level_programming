#!/usr/bin/python3
"""
A class Square with private instance attribute size
and a public instance method area
and property setter for private attribut size
with a public instance method that prints square with #
private instance attribute position
"""


class Square:
    """ define a the size of the square """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation of size and position"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieves position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def pos_set(self):
        """ prints in stdout square with # """
        pos = ""
        if self.__size == 0:
            print()
        """for a number in vertical,go to new line"""
        for i in range(self.__position[1]):
            pos += "\n"
        """ for a number in size"""
        for i in range(self.__size):
            """ for each no.in the first index,horizontal, add space"""
            for j in range(self.position[0]):
                pos += " "
            for k in range(self.size):
                pos += '#'
            pos += "\n"
        return pos

    def my_print(self):
        print(self.pos_set(), end='')

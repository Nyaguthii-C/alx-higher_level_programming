#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle
the height and width attributes of the rectangle
with public instances for area and perimeter
public class attribute that counts instances
"""


class Rectangle:
    """
    initialization of height and width
    width and height values set
    and exceptions for non integer values set

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        insantializes width and height attributes
        counts the number of instances at instantiations
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __repr__(self):
        """ return a string representation of the rectangle """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __str__(self) -> str:
        """print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ("")
        character = ""
        for column in range(self.__height):
            for row in range(self.__width):
                character += "#"
            if column < self.__height - 1:
                character += "\n"
        return (character)

    def __del__(self):
        """
        print a message whn an instance of Rectangle is deleted
        updates the number of instances upon deletion
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

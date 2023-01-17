#!/usr/bin/python3
"""
an class Rectangle that defines a rectangle
the height and width attribytes of the rectangle
"""


class Rectangle:
    """
    initialization of height and width
    width and height valus set
    and exceptions for non integer values set

    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    def width(self, value):
        if width >= 0 and width <= 9:
            def set_width(self, width):
                self.__width = value
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        return self.__height

    def height(self, value):
        if height >= 0 and height <= 9:
            def set_height(self, height):
                self.__height = value
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

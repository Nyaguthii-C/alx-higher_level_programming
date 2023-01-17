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

    def width(self):
        self.__width = width

    def width(self, value):
        if width >= 0 and width <= 9:
            def set_width(self, width):
                self.__width = width
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    def height(self):
        self.__height = height

    def height(self, value):
        if width >= 0 and width <= 9:
            def set_width(self, width):
                self.__width = width
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

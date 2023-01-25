#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


my_square = Rectangle.square(5)
a = my_square.area()
p = my_square.perimeter()
print("Area: {} - Perimeter: {}".format(a, p))
print(my_square)

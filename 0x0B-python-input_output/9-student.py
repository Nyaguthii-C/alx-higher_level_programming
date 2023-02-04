#!/usr/bin/python3
"""  a class Student that defines a student """


class Student:
    """ My class"""
    def __init__(self, first_name, last_name, age):
        """
        initializes public attributes first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the dictionary description with class Student(self) """
        return self.__dict__

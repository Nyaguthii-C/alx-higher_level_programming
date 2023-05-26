#!/usr/bin/python3
"""
a function that returns a tuple
with the length of a string and its first character
"""


def multiple_returns(sentence):
    length = len(sentence)

#    for i in range(0, len(sentence)):
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)

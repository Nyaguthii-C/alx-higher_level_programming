#!/usr/bin/python3
"""
a function that replaces all occurrences of an element
by another in a new list
"""


def search_replace(my_list, search, replace):
    def get_search(element):
        if element == search:
            return replace
        else:
            return element
    return list(map(get_search, my_list))

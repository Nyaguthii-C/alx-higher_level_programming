#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    """  function to save arguments in list to file """
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    """
    function to to add all arguments to python list
    creates object from json file
    """
    try:
        list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list = []
    list.extend(sys.argv[1:])
    save_to_json_file(list, "add_item.json")

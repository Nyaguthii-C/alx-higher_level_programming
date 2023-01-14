#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ import json module, open file and serializes my_obj into f """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

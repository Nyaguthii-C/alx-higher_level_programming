#!/usr/bin/python3
""" creates an Object from a “JSON file” """


def load_from_json_file(filename):
    """
    import json
    open file and create object  by decoding json file
    """
    import json
    with open(filename, encoding="utf-8") as f:
       return json.load(f)

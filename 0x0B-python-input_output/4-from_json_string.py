#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """ imports json module and decodes my_str """
    """ represented by json string """
    import json
    return json.loads(my_str)

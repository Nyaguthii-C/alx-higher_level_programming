#!/usr/bin/python3
""" returns the dictionary description with simple data structure """


def class_to_json(obj):
    """
        Args - obj. object will be any dat type: class, dict, list...
        Returns - dict of object
    """
    return obj.__dict__

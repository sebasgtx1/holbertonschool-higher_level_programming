#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """function that returns the dictionary description
        with simple data structure
    """
    description = {}
    if hasattr(obj, "__dict__"):
        description = obj.__dict__.copy()
    return description

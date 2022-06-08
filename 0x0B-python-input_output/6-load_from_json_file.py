#!/usr/bin/python3
"""6. Create object frm a JSON file """
from_json_string = __import__('4-from_json_string').from_json_string


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as MyJFile:
        obj = MyJFile.read()
        return from_json_string(obj)

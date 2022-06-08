#!/usr/bin/python3
""" 5. Save Object to a file """
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file
        using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        MyFile.write(to_json_string(my_obj))

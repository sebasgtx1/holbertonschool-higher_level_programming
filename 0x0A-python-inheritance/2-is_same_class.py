#!/usr/bin/python3
"""2. Exact same object:
    Write a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ Checks if obj belongs to a_class
        Return:
        True if obj belongs to a_class
        Flase otherwise
    """
    return type(obj) is a_class

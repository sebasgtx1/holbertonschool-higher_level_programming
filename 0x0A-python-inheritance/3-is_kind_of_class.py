#!/usr/bin/python3
""" 3. Same class or inherit:
    Write a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited frm
    the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ Funtion that check if obj is from a_class"""
    return isinstance(obj, a_class)

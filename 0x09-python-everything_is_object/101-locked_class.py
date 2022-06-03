#!/usr/bin/python3
""" 31. Low memory cost:
    Write a class LockedClass with no class or object
    attribute, that prevents the user from dynamically
    creating new instance attributes, except if the new
    instance attribute is called first_name.
"""


class LockedClass:
    """ Locked class that prevents high memory cost"""
    __slots__ = ['first_name']

    def __init__(self):
        """ Constructor method """
        pass

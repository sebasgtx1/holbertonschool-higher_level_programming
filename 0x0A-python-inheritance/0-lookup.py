#!/usr/bin/python3
"""0. Lookup:
    Write a function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """ Funtion that returns a list of the aviable attributes
        and methods of an object
        Return:
            a lists of the attrbs and mthds
    """

    return list(dir(obj))

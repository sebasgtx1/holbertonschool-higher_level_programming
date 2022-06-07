#!/usr/bin/python3
"""4. Only sub class of """


def inherits_from(obj, a_class):
    """ Function that returns True if obj is an instance of a_class
        or Flase otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)

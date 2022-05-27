#!/usr/bin/python3
""" 0. Integers addition - Write a function
    that adds 2 integers."""


def add_integer(a, b=98):
    """ Funtion that adds two ints or floats
        Args:
            a (int or float) : First argument
            b (int or float) : Second argument
        Return:
            a + b
    """
    if (type(a) == int or type(a) == float):
        if (type(b) == int or type(b) == float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        if not (type(a) == int or type(a) == float):
            raise TypeError("a must be an integer")

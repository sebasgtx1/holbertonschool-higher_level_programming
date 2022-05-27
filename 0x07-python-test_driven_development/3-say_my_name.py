#!/usr/bin/python3
""" 2. Say my name:
    Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ Funtions that prints My name is <first name> <last name>
        Args:
            first_name (str): first name string
            last_name (str): last name string
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

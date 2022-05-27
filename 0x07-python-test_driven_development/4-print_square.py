#!/usr/bin/python3
""" 3. Print square:
    Write a function that prints a square with the character #
"""


def print_square(size):
    """ Funtion that prints a square
        Args:
            size (int): size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format(size * "#"), end="")
        print()

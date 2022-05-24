#!/usr/bin/python3
"""1. Square with size:
    Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """ Class that defines a Square with size"""
    def __init__(self, size=0):
        """ Method that defines and initialize the size
        of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size

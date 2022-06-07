#!/usr/bin/python3
""" 11. Square #2:
    based on 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square"""
    def __init__(self, size):
        """ Constructor method """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Method that returns for the print and str calls"""
        return "[Square] {}/{}".format(self.__size, self.__size)

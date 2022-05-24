#!/usr/bin/python3
"""3. Area of a square:
    Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """ Class that defines a Square with size"""
    def __init__(self, size=0):
        """ Method that defines and initialize the size
        of the square

        Args:
            param1 (int): size of the square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Method calculates the area of the square

        Args:
            None
        Return:
            the square's area
        """
        return self.__size * self.__size

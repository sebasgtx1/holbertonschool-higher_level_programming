#!/usr/bin/python3
"""4. Access and update private attribute:
    Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """ Class that defines a Square with size"""
    def __init__(self, size=0):
        """ Method that defines and initialize the size
        of the square

        Args:
            param1 (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """size getter
        Return:
            size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value (int): size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
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

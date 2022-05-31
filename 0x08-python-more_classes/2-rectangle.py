#!/usr/bin/python3
""" 2. Area and Perimeter:
    Write a class Rectangle that defines
    a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initial constructor to create width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property to set width as a private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter to the width attribute
            Args:
                value (int): width given value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Property to set height as a private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter to the heigth attribute
            Args:
                value (int): width given value
        """
        if not isinstance(value, int):
            raise TypeError("heigt must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method to calculate the area of the rectangule
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Method to calculate the perimeter of the
        rectangule
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*self.__width + 2*self.__height

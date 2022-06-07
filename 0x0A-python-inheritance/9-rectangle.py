#!/usr/bin/python3
""" 9. Full Rectangle
    based on 8-rectangle.py
"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """ method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ clasee Rectangule"""
    def __init__(self, width, height):
        """ Constructor method """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ method that returns for print and str calls"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ method that calculates the area of the rectangle"""
        return self.__width * self.__height

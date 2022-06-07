#!/usr/bin/python3
""" 8. Rectangle
    based on 7-base_geometry.py
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

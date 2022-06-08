#!/usr/bin/python3
""" 8. Rectangle
    based on 7-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ clasee Rectangule"""
    def __init__(self, width, height):
        """ Constructor method """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

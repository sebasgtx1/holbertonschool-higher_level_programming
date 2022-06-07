#!/usr/bin/python3
"""  7. Integer validator:
    based on 6-base_geometry.py
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

#!/usr/bin/python3
"""10. and now, the Square! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """public method that retrives the print and str calls"""
        value = "[Square] ({}) ".format(self.id)
        value += "{}/{} - ".format(self.x, self.y)
        value += "{}".format(self.size)
        return value

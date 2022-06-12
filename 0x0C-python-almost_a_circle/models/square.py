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

    def update(self, *args, **kwargs):
        """public method that upddates the attributes of a rectangle object"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ public method that returns the dictionary representation
            of a Square"""
        _dict_ = {'id': 0, 'size': 0, 'x': 0, 'y': 0}

        for key, value in _dict_.items():
            _dict_[key] = getattr(self, key)
        return _dict_

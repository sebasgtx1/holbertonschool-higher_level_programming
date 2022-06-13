#!/usr/bin/python3
""" 2. first rectangle """
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method that calculates the area"""
        return self.__width * self.__height

    def display(self):
        """ public method that display the rectangle"""
        rectangle = "\n" * self.__y
        for i in range(self.__height):
            rectangle += " " * self.__x + "#" * self.__width + "\n"
        print(rectangle[:-1])

    def __str__(self):
        """ public method that retrives the print and str calls"""
        value = "[Rectangle] ({}) ".format(self.id)
        value += "{}/{} - ".format(self.x, self.y)
        value += "{}/{}".format(self.width, self.height)
        return value

    def update(self, *args, **kwargs):
        """ public method that upddates the attributes of a rectangle object"""
        if args is not None and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ public method that returns the dictionary representation
            of a rectangle"""

        _dict_ = {'id': 0, 'width': 0, 'height': 0, 'x': 0, 'y': 0}

        for key, value in _dict_.items():
            _dict_[key] = getattr(self, key)
        return _dict_

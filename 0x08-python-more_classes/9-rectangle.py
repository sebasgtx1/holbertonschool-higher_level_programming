#!/usr/bin/python3
""" 9. A square is a rectangle:
    Write a class Rectangle that defines
    a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __del__(self):
        """ Method that destorys the object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """ Method that creates a string with the
        propeties of the rectangle and allows the
        eval call
            Return:
                the rectangule in a printable form
        """
        return "Rectangle(%r, %r)" % (self.__width, self.__height)

    def __str__(self):
        """ Method that creates a string with the
        propeties of the rectangle
            Return:
                the rectangule in a printable form
        """
        rectangule = ""
        if self.__width == 0 or self.__height == 0:
            return rectangule
        for i in range(self.__height):
            rectangule += str(self.print_symbol) * self.__width + "\n"
        return rectangule[:-1]

    def __init__(self, width=0, height=0):
        """ Initial constructor to create width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*self.__width + 2*self.__height

    def bigger_or_equal(rect_1, rect_2):
        """ Method compare two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        comp = Rectangle.area(rect_1) - Rectangle.area(rect_2)
        if comp < 0:
            return rect_2
        return rect_1

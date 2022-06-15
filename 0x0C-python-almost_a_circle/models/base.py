#!/usr/bin/python3
""" 1. base class """
import json
import os
import turtle
from random import seed
from random import randint


class Base():
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that returns the JSON representation of
            a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ public method that writes the JSON string
            representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        json_list = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                json_list.append(list_objs[i].to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as MyFile:
            MyFile.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """ static method that returns the list of the JSON string
            representation json_string
        """
        my_list = []
        if json_string is not None:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """ public method that returns an instance with
            all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ public method that that returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        my_list = []

        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as MyJFile:
                obj = MyJFile.read()
                my_obj_list = cls.from_json_string(obj)
            for i in my_obj_list:
                my_list.append(cls.create(**i))

        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ public method that writes the JSON string
            representation of list_objs to a file
        """
        filename = "{}.csv".format(cls.__name__)
        json_list = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                json_list.append(list_objs[i].to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as MyFile:
            MyFile.write(cls.to_json_string(json_list))

    @classmethod
    def load_from_file_csv(cls):
        """ public method that that returns a list of instances"""
        filename = "{}.csv".format(cls.__name__)
        my_list = []

        if os.path.exists(filename):
            with open(filename, encoding="utf-8") as MyJFile:
                obj = MyJFile.read()
                my_obj_list = cls.from_json_string(obj)
            for i in my_obj_list:
                my_list.append(cls.create(**i))

        return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ public method to draw a figure """
        skk = turtle.Turtle()
        colors = ["red", "blue", "green", "purple", "orange", "black"]
        i = randint(0, 6)
        j = 0
        for Rectangle in list_rectangles:
            skk.up()
            skk.goto(Rectangle.x + j, Rectangle.y)
            skk.down()
            skk.color(colors[(i + 20) % 6])
            skk.fillcolor(colors[(i + 10) % 6])
            skk.begin_fill()
            for i in range(2):
                skk.forward(Rectangle.width)
                skk.right(90)
                skk.forward(Rectangle.height)
                skk.right(90)
            skk.end_fill()
            i += int((i % 2) + ((j + i*8) % 6)/2)
            j += 100

        i = randint(0, 6)
        j = -100
        for Square in list_squares:
            skk.up()
            skk.goto(Square.x + j, Square.y)
            skk.down()
            skk.color(colors[(i + 20) % 6])
            skk.fillcolor(colors[(i + 10) % 6])
            skk.begin_fill()
            for i in range(4):
                skk.forward(Square.size)
                skk.right(90)
            skk.end_fill()
            i += int((i % 2) + ((j + i*9) % 6)/2)
            j -= 100
        turtle.done()

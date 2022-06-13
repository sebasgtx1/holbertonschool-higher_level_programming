#!/usr/bin/python3
""" 1. base class """
import json


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
            return []
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

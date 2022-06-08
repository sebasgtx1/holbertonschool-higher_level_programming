#!/usr/bin/python3
"""11.Student to disk and reload"""


class Student:
    """ Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """ Constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation
            of a Student instance
        """
        description = self.__dict__.copy()
        if not type(attrs) is list:
            return description
        if not all(type(item) is str for item in attrs):
            return description
        if attrs is None:
            return description

        my_specifications = {}
        for i in description:
            for j in attrs:
                if i == j:
                    my_specifications[j] = description.get(i)
        return my_specifications

    def reload_from_json(self, json):
        """ """
        description = self.__dict__
        my_specifications = json
        for i in description:
            for j in my_specifications:
                if i == j:
                    description[i] = my_specifications.get(j)

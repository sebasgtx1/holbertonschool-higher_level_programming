#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """ Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """ Constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation
            of a Student instance
        """
        description = {}
        if hasattr(self, "__dict__"):
            description = self.__dict__.copy()
        return description

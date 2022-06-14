#!/usr/bin/python3
""" Test file for Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import json
from unittest.mock import patch


class BaseTests(unittest.TestCase):
    """ Suite to test Base class """
    def setUp(self):
        """ Restart the nb_objects without del """
        Base._Base__nb_objects = 0

    def test_main(self):
        """ main case """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_more_than_one_id(self):
        """ Passing two arguments to the Base
        constructor
        """
        with self.assertRaises(TypeError):
            dummy = Base(0, 1)

    def test_private(self):
        """ trying to access to the private attribute
        """
        dummy = Base()
        with self.assertRaises(AttributeError):
            dummy.__nb_objects

    def test_JSON(self):
        """ test to json string and
            from json string funtions
        """
        r1 = {"id": 8, "width": 10, "height": 6, "x": 4, "y": 9}
        r2 = {"id": 7, "width": 4, "height": 9, "x": 9, "y": 10}
        my_string = Base.to_json_string([r1, r2])
        dictionary = Base.from_json_string(my_string)
        self.assertEqual(dictionary, [r1, r2])

    def test_save_to_file_R(self):
        """ Passing None to the JSON file save Rectangle"""
        Rectangle.save_to_file(None)
        dummy = "[]\n"
        with open("Rectangle.json", encoding='utf-8') as MyFile:
            with patch('sys.stdout', new=StringIO()) as output:
                print(MyFile.read())
                self.assertEqual(output.getvalue(), dummy)

    def test_save_to_file_S(self):
        """ Passing None to the JSON file save Square"""
        Square.save_to_file(None)
        dummy = "[]\n"
        with open("Square.json", encoding='utf-8') as MyFile:
            with patch('sys.stdout', new=StringIO()) as output:
                print(MyFile.read())
                self.assertEqual(output.getvalue(), dummy)


if __name__ == '__main__':
    unittest.main(verbosity=2)

#!/usr/bin/python3
""" Test file for Base class """
import unittest
import os
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

    def test_base(self):
        """ base case """
        self.assertTrue(True)

    def test_main(self):
        """ main case """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_main_2(self):
        """ main case 2"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 1)

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

    def test_create_R(self):
        """ Testing the create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_S(self):
        """ Testing the create method"""
        s1 = Square(10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    def test_load_from_file_R(self):
        """ Testing the load from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        l_input = [r1, r2]
        Rectangle.save_to_file(l_input)
        l_output = Rectangle.load_from_file()
        i = 0
        for rect in l_output:
            self.assertEqual(str(rect), str(l_input[i]))
            i += 1

    def test_load_from_file_R2(self):
        """ Testing the load from file method """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        empty_list = Rectangle.load_from_file()
        self.assertEqual(empty_list, [])

    def test_load_from_file_S(self):
        """ Testing the load from file method"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        l_input = [s1, s2]
        Square.save_to_file(l_input)
        l_output = Square.load_from_file()
        i = 0
        for rect in l_output:
            self.assertEqual(str(rect), str(l_input[i]))
            i += 1

    def test_load_from_file_S2(self):
        """ Testing the load from file method """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        empty_list = Square.load_from_file()
        self.assertEqual(empty_list, [])

    def test_load_from_file_csv_R(self):
        """ Testing the load from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        l_input = [r1, r2]
        Rectangle.save_to_file_csv(l_input)
        l_output = Rectangle.load_from_file_csv()
        i = 0
        for rect in l_output:
            self.assertEqual(str(rect), str(l_input[i]))
            i += 1

    def test_load_from_file_csv_R2(self):
        """ Testing the load from file method """
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        empty_list = Rectangle.load_from_file_csv()
        self.assertEqual(empty_list, [])

    def test_load_from_file_csv_S(self):
        """ Testing the load from file method"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        l_input = [s1, s2]
        Square.save_to_file_csv(l_input)
        l_output = Square.load_from_file_csv()
        i = 0
        for rect in l_output:
            self.assertEqual(str(rect), str(l_input[i]))
            i += 1

    def test_load_from_file_csv_S2(self):
        """ Testing the load from file method """
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
        empty_list = Square.load_from_file_csv()
        self.assertEqual(empty_list, [])

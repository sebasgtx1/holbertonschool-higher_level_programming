#!/usr/bin/python3
""" Test file for the Square class """
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import json


class TestSquareMethods(unittest.TestCase):
    """ Suit to test the Square class """

    def setUp(self):
        """ Restart the nb objects without del """
        Base._Base__nb_objects = 0

    def test_frist_S(self):
        """ creating a square """

        s1 = Square(2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.area(), 4)
        with patch('sys.stdout', new=StringIO()) as output:
            s1.display()
            self.assertEqual(output.getvalue(), "##\n##\n")
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s2 = Square(2, 1, 3)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.area(), 4)
        with patch('sys.stdout', new=StringIO()) as output:
            s2.display()
            self.assertEqual(output.getvalue(), "\n\n\n ##\n ##\n")
        self.assertEqual(str(s2), "[Square] (2) 1/3 - 2")

    def test_checking_g_and_s_S(self):
        """ testing the exceptions in the setter cases for
            each attribute
        """
        with self.assertRaises(TypeError):
            s1 = Square("9")
        with self.assertRaises(ValueError):
            s1 = Square(-10)

    def test_update(self):
        """ Testing the update method"""
        s1 = Square(5)

        s1.update(10)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (1) 12/1 - 7")

        s1.update(id=89)
        my_str = str(s1)
        self.assertEqual(my_str, "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """ Testing the to dictionary method"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        my_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}

        for key, value in my_dict.items():
            self.assertEqual(value, s1_dictionary[key])

    def test_inheritance(self):
        """ Testing inheritance """
        new = Square(10)
        self.assertEqual(True, isinstance(new, Base))
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_attrb_error(self):
        """ Testing bad arguments """
        with self.assertRaises(TypeError):
            new = Square()

    def test_private(self):
        """ Testing private attributes """
        new = Square(10)
        with self.assertRaises(AttributeError):
            new.__size
        with self.assertRaises(AttributeError):
            new.__x
        with self.assertRaises(AttributeError):
            new.__y

    def test_checking_g_and_s_S3(self):
        """ testing assing """
        s = Square(10)
        s.size = 11
        self.assertEqual(s.size, 11)
        s.x = 4
        self.assertEqual(s.x, 4)
        s.y = 9
        self.assertEqual(r.y, 9)

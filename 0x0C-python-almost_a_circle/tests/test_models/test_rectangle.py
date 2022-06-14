#!/usr/bin/python3
""" Test file for the Rectangle class """
from models.base import Base
from models.rectangle import Rectangle
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import json


class TestRectangleMethods(unittest.TestCase):
    """ Suit to test the Rectangle class """

    def setUp(self):
        """ Restart the nb objects without del """
        Base._Base__nb_objects = 0

    def test_frist_R(self):
        """ creating a rectangle """

        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

    def test_checking_g_and_s_R(self):
        """ testing the exceptions in the setter cases for
            each attribute
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1.1, 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2.1)
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 1.1, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 1, 1.1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "1", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 1, "1")

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 1, -1)

    def test_area(self):
        """ testing the area funtion
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_display(self):
        """ testing the display funtion
        """
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), "##\n##\n")

        r2 = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_str_(self):
        """ testing the __str__ magic method"""
        my_rectangle = str(Rectangle(2, 2, 1, 1))
        self.assertEqual(my_rectangle, "[Rectangle] (1) 1/1 - 2/2")

    def test_update(self):
        """ """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        my_str = str(r1)
        self.assertEqual(my_str, "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        my_str = str(r1)
        self.assertEqual(my_str, "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        my_str = str(r1)
        self.assertEqual(my_str, "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        my_str = str(r1)
        self.assertEqual(my_str, "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        my_str = str(r1)
        self.assertEqual(my_str, "[Rectangle] (89) 4/5 - 2/3")

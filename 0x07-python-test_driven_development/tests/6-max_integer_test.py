#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class is for define the test cases for
    the max integer funtion
    """
    def testBadList(self):
        """Test case: passing a bad list """
        with self.assertRaises(TypeError):
            max_integer([2, 'Im not a number'])

    def testEmptyList(self):
        """Test case: passing an empty list """
        self.assertEqual(max_integer([]), None)

    def testGoodList(self):
        """Test case: passing a good list """
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def testGoodListNeg(self):
        """Test case: passing a good list
            with negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def testBadList2(self):
        """Test case: passing a bad list, the list
            has a tuple"""
        with self.assertRaises(TypeError):
            max_integer([(2, 3), 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)

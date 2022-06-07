#!/usr/bin/python3
""" 12. My integer:
    Write a class MyInt that inherits frm int
"""


class MyInt(int):
    """ Class MyInt"""

    def __eq__(self, other):
        """ Method that truncate == and != """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that truncate != and == """
        return int.__eq__(self, other)

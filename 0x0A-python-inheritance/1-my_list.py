#!/usr/bin/python3
"""1. My list:
    Write a class MyList that inherits from list
"""


class MyList(list):
    """ Class MyList, child of list"""

    def print_sorted(self):
        """ method that prints a list in ascending sort"""
        my_list_s = self.copy()
        my_list_s.sort()
        print(my_list_s)

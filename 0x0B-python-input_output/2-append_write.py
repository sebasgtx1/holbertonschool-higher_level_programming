#!/usr/bin/python3
"""1. Append to a file """


def append_write(filename="", text=""):
    """ function that appends a string to a text file (UTF8)
        and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as MyFile:
        chars = MyFile.write(text)
        return chars

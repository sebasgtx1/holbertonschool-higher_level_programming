#!/usr/bin/python3
"""4. Text indentation:
    Write a function that prints a text with 2 new
    lines after each of these characters: ., ?
"""


def text_indentation(text):
    """Funtion that that prints a text with 2 new
    lines after each of these characters: ., ?
        Args:
            text(str): the text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    copy = text[:]

    for delim in ".?:":
        list_text = copy.split(delim)
        copy = ""
        for i in list_text:
            i = i.strip(" ")
            if copy is "":
                copy = i + delim
            else:
                copy += "\n\n" + i + delim

    print(copy[:-3], end="")

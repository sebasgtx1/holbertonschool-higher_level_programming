#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for index in range(len(str)):
        if index != n:
            copy += str[index]
    return copy

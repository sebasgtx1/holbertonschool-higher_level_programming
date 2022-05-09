#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for i in range(len(my_list)):
        if i == 0:
            max_number = my_list[i]
        else:
            if my_list[i] > max_number:
                max_number = my_list[i]
    return max_number

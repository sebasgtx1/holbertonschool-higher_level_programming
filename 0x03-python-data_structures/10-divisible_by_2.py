#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    comp_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            comp_list.append(True)
        else:
            comp_list.append(False)
    return comp_list

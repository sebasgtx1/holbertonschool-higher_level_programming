#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(ord('a'), ord('z')+1):
            diff = 32
        else:
            diff = 0
        print("{:c}".format(ord(str[i]) - diff), end='')
    print("")

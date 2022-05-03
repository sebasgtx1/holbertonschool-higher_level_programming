#!/usr/bin/python3
for letters in range(ord('z'), ord('a')-1, -1):
    if letters % 2 == 0:
        diff = 0
    else:
        diff = 32
    print("{:c}".format(letters - diff), end="")

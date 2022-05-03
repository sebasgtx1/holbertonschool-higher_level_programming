#!/usr/bin/python3
for letters in range(ord('a'), ord('z')+1):
    if letters in [ord('q'), ord('e')]:
        continue
    print("{:c}".format(letters), end="")

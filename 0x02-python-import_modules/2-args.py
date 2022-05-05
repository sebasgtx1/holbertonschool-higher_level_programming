#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if (args == 0):
        print(f"{args} arguments.")
    elif (args == 1):
        print(f"{args} argument:")
    elif (args >= 1):
        print(f"{args} arguments:")
    if (args >= 1):
        for index in range(1, args+1):
            print(f"{index}: {sys.argv[index]}")

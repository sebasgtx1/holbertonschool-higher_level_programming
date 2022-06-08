#!/usr/bin/python3
"""7. Load, add, save """
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """ main code of the script"""
    my_list = []
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, "add_item.json")

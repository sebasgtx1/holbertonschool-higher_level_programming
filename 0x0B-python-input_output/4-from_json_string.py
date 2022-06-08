#!/usr/bin/python3
""" 4. Frm JSON string to Object"""
import json


def from_json_string(my_str):
    """ function that returns the Object representation
    of a JSON string
    """
    return json.loads(my_str)

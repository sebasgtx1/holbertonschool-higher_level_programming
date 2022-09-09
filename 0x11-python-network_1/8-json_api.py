#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if sys.argv[1] and sys.argv[1].isalpha() else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_json = r.json()
        id_, name = r_json.get("id"), r_json.get("name")
        print("[{}] {}".format(id_, name)) if r_json else print("No result")
    except ValueError:
        print('Not a valid JSON')

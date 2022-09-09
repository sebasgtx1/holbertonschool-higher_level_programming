#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("Error code: {}".format(r.status_code)) if code >= 400 else print(r.text)

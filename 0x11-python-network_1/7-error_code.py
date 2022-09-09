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
    status = r.status_code
    body = r.text
    print("Error code: {}".format(status)) if status >= 400 else print(body)

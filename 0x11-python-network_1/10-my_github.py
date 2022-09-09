#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import requests
import requests.auth
import sys


if __name__ == "__main__":
    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=basic)
    status, id_ = r.status_code, r.json().get("id")
    print('None') if status >= 400 else print(id_)

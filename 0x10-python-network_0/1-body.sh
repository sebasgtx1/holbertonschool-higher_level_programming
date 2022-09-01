#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
# -L curl flag alows any type of redirections, so, always get a 200 OK status code (the request was successful)
curl -sL "$1"

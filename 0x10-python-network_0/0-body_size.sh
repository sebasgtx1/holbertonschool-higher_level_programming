#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# -s curl flag hide progress bar output when using shell scripts
# -c wc flag print the byte counts
curl -s "$1" | wc -c

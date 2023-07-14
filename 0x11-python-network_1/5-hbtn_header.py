#!/usr/bin/python3
"""
displays the value of the X-Request-Id variable
found in the header of the response
Usage: ./1-hbtn_header.py <url>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))

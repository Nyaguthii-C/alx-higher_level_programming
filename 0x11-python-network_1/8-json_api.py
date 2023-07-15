#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    req =\
        requests.post('http://0.0.0.0:5000/search_user', data={'q': 'letter'})
    try:
        req = req.json()
        if req == {}:
            print("No result")
        else:
            print("{}{}{} {}".format("[", req['id'], "]", req['name']))
    except ValueError as e:
        print("Not a valid JSON")

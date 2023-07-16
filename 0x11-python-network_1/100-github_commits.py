#!/usr/bin/python3
"""
takes 2 arguments list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
Usage: ./100-github_commits.py rails rails
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    req = requests.get(url)
    req = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                req[i].get("sha"),
                req[i].get("commit").get("author").get("name")))
    except IndexError as e:
        pass

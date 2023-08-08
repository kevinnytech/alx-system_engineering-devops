#!/usr/bin/python3
"""A function that queries the Reddit API and prints the titles of the
first 10 hot posts
"""
from requests import request


def top_ten(subreddit):
    """A function that queries the Reddit API and returns the number
    of subscribers"""
    url = "https://api.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        for i in range(10):
            print(response['data']['children'][i]['data']['title'])
    except Exception:
        print(None)

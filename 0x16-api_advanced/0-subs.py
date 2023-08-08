#!/usr/bin/python3
"""A file to make a query to an endpoint
"""
from requests import request


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API and returns the number
    of subscribers"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        subscribers = response['data']['subscribers']
        return subscribers
    except Exception:
        return 0

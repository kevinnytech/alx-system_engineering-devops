#!/usr/bin/python3
"""A file to make a query to an endpoint
"""
from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """A recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles"""
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            hot_list.append(item['data']['title'])
        if _after is not None:
            recurse(subreddit, hot_list, _after)
        return hot_list
    except Exception:
        return None

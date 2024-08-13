#!/usr/bin/python3

"""
function that queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords
"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    headers = {"User-Agent": "reddit:top_ten:v1.0 (by /u/yourusername)"}
    params = {
            'after': after,
            'count': count,
            'limit': 100
    }
    response = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count = results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list

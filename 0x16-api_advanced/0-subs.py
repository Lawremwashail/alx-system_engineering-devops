#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscriber

"""


import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers in a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Custom User-Agent (by /u/yourself)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")

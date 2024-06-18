#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscriber

"""


import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Custom User-Agent (by /u/yourself)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()

        if 'data' in results and 'subscribers' in results['data']:
            return results['data']['subscribers']

        else:
            return 0
    elif response.status_code == 404:
        return 0
    else:
        return 0

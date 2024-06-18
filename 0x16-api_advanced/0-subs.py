#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url =  "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit=subreddit)
    headers = {
            "User-Agent": "Custom User-Agent (by /u/yourself)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            results = response.json()
            return results['data']['subscribers']
        elif response.status_code == 404:
            return 0

        else:
            return 0

    except requests.RequestException:
        return 0

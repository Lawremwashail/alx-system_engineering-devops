#!/usr/bin/python3

"""
Function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):

    """
    Recursive function that queries the Reddit API and returns a
    list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        hot_list (list, optional): A list to store the titles o
        hot articlest.
        after (str, optional): A pagination parameter for Reddit API.

    Returns:
        list or None: A list of titles of hot articles for the
        given subreddit.
        Returns None if the subreddit is invalid or
                      no results are found.
    """

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

    try:
        results = response.json().get("data", {})
        children = results.get("children", [])
        after = results.get("after")

    except ValueError:
        return None

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

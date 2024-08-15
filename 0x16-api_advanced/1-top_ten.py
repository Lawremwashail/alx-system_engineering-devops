#!/usr/bin/python3

"""
Function that queries and prints the titles of the first 10 hot posts
"""


def top_ten(subreddit):

    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        None: Prints the titles of the first 10 hot
        posts or None if the subreddit is invalid.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "reddit:top_ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})

    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)

    else:
        print(None)

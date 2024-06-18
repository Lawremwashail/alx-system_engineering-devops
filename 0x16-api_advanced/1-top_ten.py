#!/usr/bin/python3

"""
Function that queries and prints the titles of the first 10 hot posts
"""


def top_ten(subreddit):

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "reddit:top_ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')

    children = data.get("children", [])

    for child in children[:10]:
        title = child.get("data", {}).get("title")
        if title:
            print(title)

    else:
        print(None)

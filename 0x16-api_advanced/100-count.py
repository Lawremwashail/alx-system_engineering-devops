#!/usr/bin/python3
"""
Function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Counts the occurrences of specified words in the titles of hot posts
    in a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): A list of words to count.
        after (str, optional): A pagination parameter for Reddit API.
        counts (dict, optional): A dictionary to store word counts.

    Returns:
        None: Prints the counts of each word in the subreddit titles.
    """
    if not word_list or not subreddit:
        return

    headers = {"User-Agent": "your_bot:v1.0 (by /u/yourusername)"}
    params = {"limit": 100, "after": after}

    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json",
            headers=headers,
            params=params,
            allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
    except ValueError:
        return

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        title_words = title.split()

        for word in word_list:
            word_lower = word.lower()
            if word_lower in title_words:
                counts[word_lower] = counts.get(word_lower, 0)
                + title_words.count(word_lower)

    after = data.get("after")

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(
                counts.items(),
                key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

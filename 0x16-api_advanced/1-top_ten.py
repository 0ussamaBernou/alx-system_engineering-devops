#!/usr/bin/python3
"""
module to query the Reddit API and returns top ten hot posts
"""

import requests


def top_ten(subreddit):
    """Returns the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
        return
    # return None
    print("None")

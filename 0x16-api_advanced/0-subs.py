#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # add chrome on windows user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if not data:
        return 0
    try:
        subscribers = data["data"]["subscribers"]
    except Exception:
        return 0
    return subscribers

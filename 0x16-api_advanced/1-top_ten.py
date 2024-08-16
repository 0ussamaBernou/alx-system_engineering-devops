#!/usr/bin/python3
"""
Top 10 posts of a subreddit
"""

import requests


def top_ten(subreddit):
    """Get the top 10 posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers)
    data = response.json()
    if "data" in data:
        posts = data["data"]["children"]
        [print(post["data"]["title"]) for post in posts]
        return
    elif data["message"] != "Not Found":
        print("None")
        return

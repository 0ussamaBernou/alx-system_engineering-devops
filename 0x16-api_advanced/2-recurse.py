#!/usr/bin/python3
"""
Recursively query reddit for a given subreddit hot posts

"""

import requests


def recurse(
    subreddit: str, hot_list: list[str] = []
) -> list[str] | None:
    """
    Query reddit for hot posts
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json",
            headers=headers,
            allow_redirects=False,
        )
    except Exception:
        return None
    hot_posts = response.json()
    hot_posts = hot_posts["data"]["children"]

    try:
        hot_list.append(hot_posts[len(hot_list)]["data"]["title"])
    except Exception:
        return hot_list

    recurse(subreddit, hot_list)

    return hot_list

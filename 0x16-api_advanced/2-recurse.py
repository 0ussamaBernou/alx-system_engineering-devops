#!/usr/bin/python3
"""
module to query the Reddit API and returns all  hot posts recursively
"""

import requests
import rich


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Returns the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={"limit": 100, "after": after or None},
    )

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))

        data_after = response.json().get("data").get("after")
        if data_after is not None:
            return recurse(
                subreddit,
                hot_list,
                count + len(response.json().get("data").get("children")),
                data_after,
            )
        return hot_list
    return None

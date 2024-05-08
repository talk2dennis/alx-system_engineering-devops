#!/usr/bin/python3
"""
    A python script that returns the top 10 post
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
     a recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.
        If no results are found for the given subreddit, the function should
        return None.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    try:
        response = requests.get(url, headers=headers, params={"limit": 100})
        if response.status_code == 200:
            data = response.json()
            children = data["data"]["children"]
            for child in children:
                hot_list.append(child["data"]["title"])
            if data["data"]["after"] is not None:
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None

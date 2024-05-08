#!/usr/bin/python3
"""
    A python script that returns the top 10 post
"""
import json
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and prints the titles of the first
        10 hot posts listed for a given subreddit.

    Keyword arguments:
    subreddit -- a string representing the subreddit name
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, params={"limit": 10})
        if response.status_code == 200:
            data = response.json()
            children = data["data"]["children"]
            titles = [child["data"]["title"] for child in children]
            return json.dumps({"titles": titles})
        else:
            print("None")
    except Exception as e:
        print("None")
        return

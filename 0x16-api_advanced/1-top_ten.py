#!/usr/bin/python3
"""
    A python script that returns the top 10 post
"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles of the first
            10 hot posts listed for a given subreddit.

    Keyword arguments: subreddit (a string)
    Return: top 10 post
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    param = {"limit": 10}
    header = headers = {"User-Agent": "MyRedditBot/1.0"}
    res = requests.get(url, headers=header, params=param,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data")
        for child in data.get("children"):
            print(child.get("data").get("title"))
    else:
        print("None")

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
        print("None")
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    try:
        response = requests.get(url, headers=headers, params={"limit": 8})
        if response.status_code == 200:
            data = response.json()
            children = data["data"]["children"]
            for child in children:
                print(child["data"]["title"])
        else:
            print("None")
    except Exception as e:
        print("None")

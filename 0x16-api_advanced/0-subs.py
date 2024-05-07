#!/usr/bin/python3
"""
    A python script to retrieve the number of all subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function to return the number of subscribers of a subreddit

    Keyword arguments: subreddit (a string)
    Return: return the number of subscribers of a subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0

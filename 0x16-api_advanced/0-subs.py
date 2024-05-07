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
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'myReddictBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')

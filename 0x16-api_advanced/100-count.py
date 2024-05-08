#!/usr/bin/python3
""" A python script that returns the sorted number of subscribers
    of a subreddit """
import requests


def count_words(subreddit, word_list, word_dict={}, after=None):
    """Returns the sorted count of given keywords in subreddit titles"""
    if not subreddit or not isinstance(subreddit, str):
        return None

    if not word_dict:
        for word in word_list:
            word_dict[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        params = {'limit': 100}
        if after:
            params['after'] = after

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            children = data["data"]["children"]
            for child in children:
                title_words = [word.lower() for word in
                               child['data']['title'].split()]
                for word in title_words:
                    if word in word_dict:
                        word_dict[word] += 1

            if data["data"]["after"] is not None:
                return count_words(subreddit, word_list,
                                   word_dict, after=data["data"]["after"])
            else:
                sorted_word_dict = sorted(word_dict.items(),
                                          key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_dict:
                    if count > 0:
                        print(f"{word}: {count}")
                return "None"
        else:
            return None
    except Exception as e:
        return None

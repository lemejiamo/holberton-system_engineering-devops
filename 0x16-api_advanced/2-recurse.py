#!/usr/bin/python3
"""Module for advance API exercices"""
import requests

url = 'http://reddit.com/r/{}/hot.json'

def recurse(subreddit, hot_list=[], after=None):
    """Fetchers all hot posts of a subreddit"""
    headers = {"User-Agent": "Unix:0-subs:v1"}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != 'null':
            params['after'] = after
        else:
            return hot_list
    response = requests.get(url.format(subreddit),
                            headers=headers,
                            params=params)
    if response.status_code != 200:
        return None
    for elem in response.json()['data']['children']:
        hot_list.append(elem['data']['title'])
    after = response.json()['data']['after']
    if after is None:
        after = 'null'
    return recurse(subreddit, hot_list, after)

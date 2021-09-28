#!/usr/bin/python3
"""module to testnig with Reddit API Educative project"""


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0

    import requests
    headers = {'User-Agent': 'holbi/0.0.1'}
    url = 'https://www.reddit.com/r/' + subreddit + "/about/.json"
    response = requests.get(url, headers=headers).json()
    
    try:
        response['data']['subscribers']
        return (response['data']['subscribers'])
    except:
        return (0)

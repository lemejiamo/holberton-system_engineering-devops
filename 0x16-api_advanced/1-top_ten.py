#!/usr/bin/python3
"""module to testnig with Reddit API Educative project"""


def top_ten(subreddit):
    if subreddit is None:
        return 0

    import requests

    headers = {'User-Agent': 'holbi/0.0.1'}
    url = ('https://www.reddit.com/r/' +
           subreddit +
           '/hot/.json?count=10&limit=10')
    response = requests.get(url, headers=headers, allow_redirects=False).json()

    try:
        for hot in response['data']['children']:
            print(hot['data']['title'])
    except:
        return None

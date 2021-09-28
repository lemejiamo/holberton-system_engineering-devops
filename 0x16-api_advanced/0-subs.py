#!/usr/bin/python3
"""module to testnig with Reddit API Educative project"""


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0

    import requests

    CLIENT_ID = 'VltlBDVA0mgn4dp-v9mRrQ'
    SECRET_KEY = 'V1wgaUKJ8hni0EsscAWZYXGlLE7gUQ'

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {'grant_type': 'password',
            'username': 'Lemejiamo',
            'password': 'L7Vap.F?T0BO'}

    headers = {'User-Agent': 'holbi/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']

    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}


    url = 'https://oauth.reddit.com/r/' + subreddit + "/about/.json"
    response = requests.get(url, headers=headers).json()
    try:
        response['data']['subscribers']
        return (response['data']['subscribers'])
    except:
        return (0)

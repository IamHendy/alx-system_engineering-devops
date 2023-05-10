#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0."""
import requests

def number_of_subscribers(subreddit):
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Construct URL to query API for subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Query API and parse JSON response
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


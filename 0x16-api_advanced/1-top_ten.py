#!/usr/bin/python3
import requests
"""Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""

def top_ten(subreddit):
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Construct URL to query API for subreddit hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Query API and parse JSON response
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)

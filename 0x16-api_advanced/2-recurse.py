#!/usr/bin/python3
import requests

"""Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])
Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
If not a valid subreddit, return None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects."""
import requests

def recurse(subreddit, hot_list=None, after=None):
    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Initialize hot_list if it's None
    if hot_list is None:
        hot_list = []
    
    # Construct URL to query API for subreddit hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(subreddit, after)
    
    # If after parameter is present, add it to URL to get next page of results
    if after:
        url += '&after={}'.format(after)
    
    # Query API and parse JSON response
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        
        # Add titles of hot posts to list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        
        # If there are more results, recursively call function with after parameter
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
        
        # If there are no more results, return hot_list
        return hot_list
    else:
        return None


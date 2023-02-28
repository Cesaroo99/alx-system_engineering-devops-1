#!/usr/bin/python3
"""Function to query subscribers on a given reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscrebers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    response = request.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

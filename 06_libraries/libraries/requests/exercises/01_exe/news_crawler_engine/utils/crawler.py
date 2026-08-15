"""
Python Core - 06 Libraries (requests)
Exercise 3: The News Crawler Engine (Hard - Architecture & Integration)
File: crawler.py

Rules:
1. Import 'requests' and import your '@network_monitor' decorator from 'utils'.
2. Create a function 'get_top_story_ids()' decorated with '@network_monitor'.
   - Make a GET request to: "https://hacker-news.firebaseio.com/v0/topstories.json" with 'timeout=5'.
   - Parse the JSON response (which is a large list of integer IDs).
   - Return only a slice containing the FIRST 5 IDs from that list.
3. Create a function 'get_story_details(story_id: int)' decorated with '@network_monitor'.
   - Make a GET request to: f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json" with 'timeout=5'.
   - Parse and return the JSON dictionary of the story.
"""

import requests
from utils.decorators import network_monitor

@network_monitor
def get_top_story_ids():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    ids = response.json()
    if ids == []:
        return None
    return ids[:5]

@network_monitor
def get_story_details(story_id: int):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    storys = response.json()
    if storys == []:
        return None
    return storys




"""
Python Core - 06 Libraries (requests)
Exercise 3: The News Crawler Engine (Hard - Architecture & Integration)
File: main.py

Rules:
1. Import 'os', 'json', and the functions from 'crawler'.
2. Call 'get_top_story_ids()'. If it returns None, print an offline warning message and terminate the script.
3. Create an empty list called 'filtered_news' to store our processed articles.
4. Loop through the 5 IDs and call 'get_story_details(story_id)' for each one.
5. Business Rule (Filtering): Only accept stories that have a 'score' GREATER THAN OR EQUAL TO 50.
6. For each approved story, build a clean dictionary containing only:
   - 'title': The story title
   - 'author': The author ('by')
   - 'score': The score
   - 'url': The link (if 'url' key is missing, default to "No link available")
7. Append the clean dictionary to 'filtered_news'.
8. Use 'os.path.join(os.path.dirname(__file__), "top_news.json")' to define a secure local path.
9. Use a Context Manager ('with open(...)') in write mode and 'json.dump(..., indent=4)' to save 'filtered_news'.
10. Print a final summary: "Evaluated X stories. Saved Y high-relevance stories to local backup!"
"""

import os
import json
import sys
from utils import crawler

story_ids = crawler.get_top_story_ids()

if story_ids is None:
    print("Offline: não foi possível buscar as notícias.")
    sys.exit()

filtered_news = []
cont = 0
for id in story_ids:
    temp = crawler.get_story_details(id)
    if temp['score'] >= 50:
        valid_story = {
            "title": temp['title'],
            "author": temp['by'],
            "score": temp['score'],
            "url": temp.get('url', "No link available")
        }
        cont += 1
        filtered_news.append(valid_story)
       
file_path = os.path.join(os.path.dirname(__file__), "top_news.json")
with open(file_path, "w",newline="") as file:
    json.dump(filtered_news,file,indent=4)

print(f"Evaluated 5 stories. Saved {cont} high-relevance stories to local backup!")

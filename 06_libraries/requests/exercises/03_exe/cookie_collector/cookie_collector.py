"""
Python Core - 06 Libraries (requests)
Exercise 7: The Cookie Collector (Easy - Fixation)
Folder: 07_cookie_collector/
Main File: main.py

Rules:
1. Import the 'requests' module.
2. Instantiate a session object using 'session = requests.Session()'.
3. In web scraping, servers often give you tracking or session cookies on your first visit.
   We will simulate this by hitting: url_set = "https://httpbin.org/cookies/set/user_role/administrator"
4. Make a GET request to 'url_set' using your 'session' object with a 'timeout=5'.
5. Do NOT manually extract or save the cookie. Let the Session object handle it!
6. Now, make a second GET request using the same 'session' object to: url_check = "https://httpbin.org/cookies"
7. Parse the JSON response from the second request and print it to the terminal.
8. Verify that the terminal output proves the session automatically stored and sent back the "user_role": "administrator" cookie!
9. Properly close the session at the end of the script using 'session.close()'.
"""

import requests

session = requests.Session()
url_set = "https://httpbin.org/cookies/set/user_role/administrator"
url_check = "https://httpbin.org/cookies"

try:
    res1 = session.get(url_set, timeout=5)
    res1.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"[ERROR] {e}.")

try:
    res2 = session.get(url_check, timeout=5)
    res2.raise_for_status()
    print(f"Cookies user JSON 2° request: \n{res2.json()}")
    print("="*60 + "\n")
except requests.exceptions.HTTPError as e:
    print(f"[ERROR] {e}.")
finally:
    session.close()

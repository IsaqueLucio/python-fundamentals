"""
Python Core - 06 Libraries (requests)
Exercise 5: The Authenticated GitHub Client (Intermediate - Logic & Interpretation)
Folder: 05_authenticated_github_client/
Main File: main.py

Rules:
1. Import 'requests' and 'os'.
2. The GitHub API rate-limits unauthenticated scripts very strictly, but allows authenticated requests to inspect user data.
3. Define the URL to check a user's profile: url = "https://api.github.com/users/torvalds"
4. Create a dictionary named 'auth_headers'. Add an "Accept" header with the value: "application/vnd.github+json".
5. We want to simulate passing a Bearer token. Add an "Authorization" key to your 'auth_headers' with the value: "Bearer invalid_secret_token_test_12345".
6. Make a GET request passing these headers and 'timeout=5'.
7. We EXPECT this request to fail because the token is intentionally invalid! 
   Instead of crashing, check 'response.status_code'.
8. If the status code is 401 (Unauthorized), print a clean warning: 
   "[AUTH BLOCK] The GitHub server rejected our Bearer token! Status: 401 Unauthorized".
9. Now, make a SECOND request to the same URL, but this time do NOT pass the 'auth_headers' (make an unauthenticated public request).
10. If this second request succeeds (Status 200), parse the JSON and print Linus Torvalds' "name", "company", and "public_repos"!
"""

import requests

url = "https://api.github.com/users/torvalds"
token = "invalid_secret_token_test_12345"

auth_headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"    
}

try:
    response = requests.get(url, headers=auth_headers, timeout=5)
    if response.status_code == 401:
        print("[AUTH BLOCK] The GitHub server rejected our Bearer token! Status: 401 Unauthorized")
except requests.exceptions.HTTPError as e:
    print(f"ERROR: {e}.")

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status
    data = None
    if response.status_code == 200:
        data = response.json()
        print(f"Linus Torvalds\nName: {data['name']}\nCompany: {data['company']}\nPublic Repos: {data['public_repos']}")
except requests.exceptions.HTTPError as e:
    print(f"ERROR: {e}.")
"""
Python Core - 06 Libraries
Module: requests
File: 01_http_basics.py
Description: Understanding HTTP methods, response codes, query parameters, and JSON parsing.
"""
import requests

print("--- 1. A Simple GET Request (Fetching Data) ---")
# We will use 'jsonplaceholder', a free public API for testing and prototyping.
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(f"Status Code: {response.status_code}") # 200 means OK!
print(f"Content-Type: {response.headers['Content-Type']}")

# Since the server returns JSON, requests can automatically parse it into a Python dictionary!
user_data = response.json()
print(f"User Found: {user_data['name']} | Email: {user_data['email']}\n")


print("--- 2. Passing Query Parameters (Filtering Data) ---")
# Instead of hardcoding "?postId=1" in the URL, we pass a dictionary to the 'params' argument.
# This cleanly formats the URL to: https://jsonplaceholder.typicode.com/comments?postId=1
base_url = "https://jsonplaceholder.typicode.com/comments"
query_params = {"postId": 1}

response = requests.get(base_url, params=query_params)
comments = response.json()

print(f"Fetched {len(comments)} comments for Post ID 1.")
print(f"First comment author: {comments[0]['email']}\n")


print("--- 3. Handling HTTP Errors and Timeouts (Defensive Coding) ---")
# In real-world apps, servers go down, URLs change (404), or requests hang forever.
# We MUST always use 'timeout' and intercept exceptions!

invalid_url = "https://jsonplaceholder.typicode.com/invalid_endpoint_999"

try:
    # timeout=5 means: "if the server doesn't respond in 5 seconds, drop the connection!"
    res = requests.get(invalid_url, timeout=5)
    
    # This automatically raises an HTTPError if the status code is 4xx (Client Error) or 5xx (Server Error)
    res.raise_for_status()
    
    print("Data retrieved successfully!")

except requests.exceptions.HTTPError as err_http:
    print(f"[HTTP ERROR] The server returned an error code: {err_http}")

except requests.exceptions.Timeout:
    print("[TIMEOUT] The server took too long to respond!")

except requests.exceptions.ConnectionError:
    print("[CONNECTION ERROR] No internet connection or server is completely offline.")

except Exception as e:
    print(f"[CRITICAL] An unexpected error occurred: {e}")
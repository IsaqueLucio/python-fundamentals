"""
Python Core - 06 Libraries (requests)
Exercise 6: The OAuth Token Interceptor (Hard - Problem Solving & Architecture)
Folder: 06_oauth_token_interceptor/
Main File: main.py

Rules:
1. Import 'requests' and 'time'.
2. In enterprise systems, access tokens expire. When an API returns '401 Unauthorized', a robust software engine must intercept this error, request a fresh token, and automatically retry the failed request!
3. We will simulate this using httpbin.org endpoints.
4. Create a function 'get_fresh_token()' that simulates logging into an auth server:
   - It should print "[AUTH ENGINE] Token expired or missing. Requesting fresh token..."
   - Return a simulated token string: "fresh_valid_token_999"
5. Create a function 'fetch_protected_resource(token: str)' decorated with or using basic error handling:
   - Target URL: f"https://httpbin.org/bearer"
   - Send the token in the headers: {"Authorization": f"Bearer {token}"}
   - Set 'timeout=5'.
   - Return the response object directly.
6. In your main execution flow:
   - Start with an old token variable: current_token = "old_expired_token_000"
   - To SIMULATE a 401 rejection on your first attempt, let's intentionally test against httpbin's basic-auth endpoint first, OR check our response logic:
   - Actually, let's build the real interceptor logic! Make a request using 'fetch_protected_resource(current_token)'.
   - Check if 'response.status_code == 200'. If it is, print "[SUCCESS] Resource accessed!" and print the JSON.
   - BUT, to prove your interceptor works, let's force a failure condition: 
     Create a loop or a control structure where if a hypothetical check (or a real 401 status code if testing against an endpoint that rejects old tokens) fails, your script calls 'current_token = get_fresh_token()' and re-runs 'fetch_protected_resource(current_token)'.
7. TO MAKE IT 100% REALISTIC AND TESTABLE against httpbin.org:
   - Step A: Attempt to fetch data from url = "https://httpbin.org/status/401" (This endpoint ALWAYS returns a 401 Unauthorized status code, simulating our token rejection!).
   - Step B: Check if the status code is 401. If it is, catch it! Print "[INTERCEPTOR] 401 Unauthorized detected! Token is invalid."
   - Step C: Call 'get_fresh_token()' and save the new string into 'current_token'.
   - Step D: Now, make the final retry request to "https://httpbin.org/bearer" passing the NEW 'current_token' in the Authorization header!
   - Step E: Verify this second request returns 200 OK, and print the JSON proving the payload was successfully retrieved after the automatic token refresh!
"""

import requests

current_token = "old_expired_token_000"

def get_fresh_token() -> str:
    print("[AUTH ENGINE] Token expired or missing. Requesting fresh token...")
    return "fresh_valid_token_999"

def check_status_code(status_code, json_data = None):
      global current_token
      if status_code == 200:
          print("[SUCCESS] Resource accessed!")
          print(json_data)
      elif status_code == 401:
           print("[INTERCEPTOR] 401 Unauthorized detected! Token is invalid.")
           current_token = get_fresh_token()
           fetch_protected_resource(current_token)

def fetch_protected_resource(token: str, url = f"https://httpbin.org/bearer"):

   auth_header = {"Authorization": f"Bearer {token}"}
   try:
        response = requests.get(url, headers=auth_header, timeout=15)
        status_code = response.status_code
        print(status_code)
        if status_code == 200:
             data = response.json()
             check_status_code(status_code, data)
        else:
            check_status_code(status_code)
        return response
   except requests.exceptions.ReadTimeout:
        print("[ERROR] The server took a long time to respond.")

fetch_protected_resource(current_token)
fetch_protected_resource(current_token,url = f"https://httpbin.org/status/401")


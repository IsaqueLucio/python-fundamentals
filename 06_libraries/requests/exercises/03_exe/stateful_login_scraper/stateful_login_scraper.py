"""
Python Core - 06 Libraries (requests)
Exercise 9: The Stateful Login Scraper (Hard - Problem Solving & Architecture)
Folder: 09_stateful_login_scraper/
Main File: main.py

Rules:
1. Import 'requests'.
2. You are building an automated scraper for a dashboard that requires a multi-step stateful authentication flow.
3. Open a persistent session using a Context Manager: 'with requests.Session() as session:'
4. Step A (Global Configuration):
   - Update the session headers ONCE to disguise your scraper as a real browser:
     session.headers.update({"User-Agent": "StatefulScraperEngine/3.0", "Accept": "application/json"})
5. Step B (Simulating the Login Handshake):
   - To enter the dashboard, the server requires an active authentication cookie.
   - Hit the simulated login endpoint: login_url = "https://httpbin.org/cookies/set/auth_session_id/secure_token_884422"
   - Use 'session.get(login_url, timeout=5)' and check that 'response.status_code == 200'.
   - Print a message confirming that the login handshake was successful.
6. Step C (Scraping the Protected Dashboard):
   - Now that the session holds both the custom User-Agent and the login cookie, access the protected resource:
     dashboard_url = "https://httpbin.org/anything/admin/dashboard"
   - Make a GET request to 'dashboard_url' using the session.
7. Step D (Verification & Data Extraction):
   - Verify the request succeeded (status code 200).
   - Parse the JSON response returned by 'httpbin.org/anything/' (which echoes back everything the server received).
   - Extract and print:
     1. The exact URL that was reached ('url' key).
     2. The "User-Agent" received by the server (inside the 'headers' dictionary).
     3. The "auth_session_id" cookie received by the server (inside the 'headers' or 'cookies' dictionary).
8. Print a final verification message confirming that the multi-step stateful scraping pipeline executed without dropping the session state!
"""

import requests

with requests.Session() as session:
   try:
      session.headers.update({
         "User-Agent": "StatefulScraperEngine/3.0",
         "Accept": "application/json"
      })
      login_url = "https://httpbin.org/cookies/set/auth_session_id/secure_token_884422"
      res1 = session.get(login_url, timeout=5)
      res1.raise_for_status()
      print("[SUCCESS] The login handshake was successful.\n")
      dashboard_url = "https://httpbin.org/anything/admin/dashboard"
      res2 = session.get(dashboard_url, timeout=5)
      res2.raise_for_status()
      print("[SUCCESS] The dashboard was successfully reached.\n")
      data_json = res2.json()
      print("[SUCCESS] Dashboard JSON data: \n"
            f"URL: {data_json['url']}\n"
            f"USER-AGENT: {data_json['headers']['User-Agent']}\n"
            f"COOKIES[auth_session_id]: {data_json['headers']['Cookie']}\n")
      print("Verification complete: the multi-step, stateful scraping pipeline "
      "executed successfully — session state was preserved across all requests, "
      "with no loss of the authentication token throughout the run.")
   except requests.exceptions.HTTPError as e:
      print(f"[HTTP ERROR]: {e}")
   except requests.exceptions.ConnectionError as e:
      print(f"[CONNECTION ERROR]: {e}")
   except requests.exceptions.RequestException as e:
      print(f"[REQUEST ERROR]: {e}")

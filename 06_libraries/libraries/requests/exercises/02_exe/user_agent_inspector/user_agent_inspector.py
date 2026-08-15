"""
Python Core - 06 Libraries (requests)
Exercise 4: The User-Agent Inspector (Easy - Fixation)
Folder: 04_user_agent_inspector/
Main File: main.py

Rules:
1. Import the 'requests' module.
2. Define a target URL: url = "https://httpbin.org/user-agent"
3. Create a dictionary named 'custom_headers' with a specific "User-Agent":
   "Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
   (This disguises your Python script as an iPad browser!).
4. Make a GET request to the URL passing your 'custom_headers' and setting 'timeout=5'.
5. Use a 'try/except' block to catch 'requests.exceptions.RequestException' in case httpbin.org is unstable or times out.
6. If successful, print the status code and print the exact JSON response returned by the server to prove it recognized your iPad User-Agent!
"""

import requests

url = "https://httpbin.org/user-agent"

custom_headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8",
    "X-Custom-Client-App": "PythonCore-DeepDive/1.0"
}

try:
   response = requests.get(url, headers=custom_headers, timeout=5)
   response.raise_for_status()
   data = response.json()
   
   print(f"Status Code: {response.status_code}\n"
         f"JSON response: \n{data}")
except requests.exceptions.RequestException as e:
   print(f"ERROR: {e}.")   
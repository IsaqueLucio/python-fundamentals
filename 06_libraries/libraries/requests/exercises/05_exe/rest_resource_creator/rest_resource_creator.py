"""
Python Core - 06 Libraries (requests)
Exercise 13: The REST Resource Creator (Easy - Fixation)
Folder: 13_rest_resource_creator/
Main File: main.py

Rules:
1. Import the 'requests' module.
2. Define the target URL for creating a resource: url = "https://jsonplaceholder.typicode.com/users"
3. Create a Python dictionary named 'new_user' representing a system user with these exact fields:
   - "name": "Isaque"
   - "username": "isaque_dev"
   - "email": "isaque@dev.com"
   - "role": "Data Engineer"
4. Send a POST request to 'url' passing your 'new_user' dictionary to the 'json=' parameter with 'timeout=5'.
5. Check if 'response.status_code == 201' (201 Created is the REST standard for resource creation).
6. If the creation succeeded, print a confirmation message showing the exact status code.
7. Parse and print the JSON returned by the server to prove that the server received your data and generated a new ID for the user!
"""

import requests

base_url = "https://jsonplaceholder.typicode.com/users"

new_user = {
    "name": "Joe",
    "username": "Robin",
    "email": "joe_robin@mail.com",
    "role": "QA"
}

try:
   response = requests.post(base_url,json=new_user, timeout=5)
   response.raise_for_status()
   if response.status_code == 201:
      print("[SUCCESS] Status Code: 201.")
      print("Server Response (with generated ID):")
      print(response.json())
except requests.exceptions.RequestException as e:
    print(f"[ERROR]: {e}.")   


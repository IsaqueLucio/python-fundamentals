"""
Python Core - 06 Libraries (requests)
Exercise 14: The CRUD Lifecycle Manager (Intermediate - Logic & Interpretation)
Folder: 14_crud_lifecycle_manager/
Main File: main.py

Rules:
1. Import 'requests'.
2. You must execute a full CRUD lifecycle on a single resource using 'https://jsonplaceholder.typicode.com/posts/10'.
3. Step A (READ): 
   - Send a GET request to the target URL. 
   - Verify it returns 200 OK and print the original "title" of the post.
4. Step B (FULL REPLACE - PUT):
   - Create a payload dictionary replacing ALL fields: {"id": 10, "title": "Updated Title", "body": "Updated Body", "userId": 1}
   - Send a PUT request passing this dictionary to 'json='.
   - Verify the response status code is 200 OK and print the new title returned by the server.
5. Step C (PARTIAL UPDATE - PATCH):
   - Now, we only want to update the title without sending the body or userId.
   - Create a smaller dictionary: {"title": "Patched Title Only"}
   - Send a PATCH request passing this dictionary to 'json='.
   - Verify the status code is 200 OK and print the patched title returned by the server.
6. Step D (DELETE):
   - Send a DELETE request to the target URL.
   - Verify that the server responds with status code 200 OK (or 204 No Content).
   - Print a clean summary report confirming that all 4 lifecycle phases (GET, PUT, PATCH, DELETE) executed successfully!
"""

import requests
import json

base_url = "https://jsonplaceholder.typicode.com/posts/10"
print("CRUD means Create, Read, Update and Delete\n")
try: 
    print("--------------CRUD LIFECYCLE | C.Read.U.D--------------\n")
    print(f"Trying to read the URL {base_url} content:...")
    res_read = requests.get(base_url, timeout=5)
    res_read.raise_for_status()
    print("[SUCCESS] Url Content:")
    print(json.dumps(res_read.json(),indent=4,ensure_ascii=False))
    print("=" * 60 + "\n")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")


payload_dict = {
    "id": 10, 
    "title": "Updated Title", 
    "body": "Updated Body", 
    "userId": 1
    }

try:
   print("--------------CRUD LIFECYCLE | C.R.Update.D--------------\n")
   print("There are two types of updates: " \
   "using PUT (complete replacement of the entire object) "
   "and using PATCH (partial replacement, affecting only the desired parameter).")
   print(f"\nTrying to update the object using [PUT] on the URL {base_url}... ")
   res_put = requests.put(base_url, json=payload_dict, timeout=5)
   res_put.raise_for_status()
   print("[SUCCESS] The object was updated using PUT. Updated content from the URL:")
   print(json.dumps(res_put.json(),indent=4, ensure_ascii=False))
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")


partial_payload = {"title": "Patched Title Only"}

try:
   print(f"\nAttempting to partially update the object using [PATCH] at URL {base_url}... ")
   res_patch = requests.patch(base_url,json=partial_payload,timeout=5)
   res_patch.raise_for_status()
   print("[SUCCESS] The object was updated using PATCH. Partially updated content from the URL:")
   print(json.dumps(res_patch.json(),indent=4,ensure_ascii=False))
   print("=" * 60 + "\n")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")

try:
    print("--------------CRUD LIFECYCLE | C.R.U.Delete--------------\n")
    print(f"Trying to delete the URL {base_url} content:...")
    res_del = requests.delete(base_url,timeout=5)
    res_del.raise_for_status()
    print("[SUCCESS] URL content successfully deleted. URL content: ")
    print(res_del.json())
    print("=" * 60 + "\n")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")


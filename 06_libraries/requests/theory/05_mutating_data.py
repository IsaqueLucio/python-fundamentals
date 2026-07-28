"""
Python Core - 06 Libraries
Module: requests
File: 05_mutating_data.py
Description: Mastering RESTful CRUD operations (POST, PUT, PATCH, DELETE) and multipart file uploads.
"""
import requests
import os

# We use JSONPlaceholder, the industry-standard free fake API for testing RESTful CRUD operations:
BASE_URL = "https://jsonplaceholder.typicode.com"

print("--- 1. CREATE: Sending JSON Payloads with POST ---")
# To create a new resource, we send a POST request with a dictionary passed to the 'json=' parameter.
new_post_payload = {
    "title": "Python Core Deep Dive",
    "body": "Mastering HTTP mutations and RESTful architectures.",
    "userId": 101
}

try:
    res_post = requests.post(f"{BASE_URL}/posts", json=new_post_payload, timeout=5)
    res_post.raise_for_status()
    
    # 201 Created is the standard HTTP status code for successful resource creation!
    print(f"Status Code: {res_post.status_code} (Created)")
    print("Server Response (with generated ID):")
    print(res_post.json())
except requests.exceptions.RequestException as e:
    print(f"[POST ERROR] {e}")

print("\n" + "="*60 + "\n")


print("--- 2. UPDATE: Full Replacement (PUT) vs Partial Modification (PATCH) ---")
# Let's target an existing resource: Post ID 1
target_url = f"{BASE_URL}/posts/1"

# PUT replaces the ENTIRE resource. If you leave out a field, it might get overwritten as null!
put_payload = {
    "id": 1,
    "title": "Completely Replaced Title",
    "body": "Completely replaced body content.",
    "userId": 1
}
res_put = requests.put(target_url, json=put_payload, timeout=5)
print(f"PUT Status Code:   {res_put.status_code} (OK)")
print(f"PUT Result Title:  {res_put.json()['title']}")

# PATCH modifies ONLY the fields you send, leaving the rest of the resource intact!
patch_payload = {
    "title": "Patched Title Only"
}
res_patch = requests.patch(target_url, json=patch_payload, timeout=5)
print(f"\nPATCH Status Code: {res_patch.status_code} (OK)")
print(f"PATCH Result Title: {res_patch.json()['title']}")

print("\n" + "="*60 + "\n")


print("--- 3. DELETE: Removing Resources Safely ---")
# DELETE removes the resource from the server.
try:
    res_delete = requests.delete(target_url, timeout=5)
    res_delete.raise_for_status()
    
    # Many REST APIs return 200 OK (with empty JSON) or 204 No Content (no body at all).
    print(f"DELETE Status Code: {res_delete.status_code}")
    print("Resource successfully deleted from server!")
except requests.exceptions.RequestException as e:
    print(f"[DELETE ERROR] {e}")

print("\n" + "="*60 + "\n")


print("--- 4. MULTIPART UPLOADS: Uploading Physical Files ---")
# To upload files, we use the 'files=' parameter.
# We will use httpbin.org/post, which echoes back files it receives!
url_upload = "https://httpbin.org/post"
test_filename = "sample_upload.txt"

# Create a temporary local file to upload:
with open(test_filename, "w", encoding="utf-8") as f:
    f.write("This is a test file for multipart upload in Python Core!")

try:
    # Syntax: files = {"field_name": open("filepath", "mode")}
    # Notice: Always open files in binary read mode ('rb') when uploading over HTTP!
    with open(test_filename, "rb") as file_to_upload:
        files_payload = {"attachment": file_to_upload}
        
        # We can even send standard form data alongside the file using 'data='!
        form_data = {"user": "Isaque", "description": "Weekly log report"}
        
        res_upload = requests.post(url_upload, files=files_payload, data=form_data, timeout=10)
        res_upload.raise_for_status()
        
        print("Upload Successful! What the server received:")
        response_data = res_upload.json()
        print(f"Form Data received: {response_data['form']}")
        print(f"File Content received: {response_data['files']['attachment']}")

except requests.exceptions.RequestException as e:
    print(f"[UPLOAD ERROR] {e}")

finally:
    # Clean up local file:
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print("\nTemporary upload file cleaned up from disk.")
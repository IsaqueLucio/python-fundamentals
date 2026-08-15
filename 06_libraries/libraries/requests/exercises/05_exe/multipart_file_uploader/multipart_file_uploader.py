"""
Python Core - 06 Libraries (requests)
Exercise 15: The Multipart File Uploader (Hard - Problem Solving & Integration)
Folder: 15_multipart_file_uploader/
Main File: main.py

Rules:
1. Import 'requests', 'json', and 'os'.
2. You are building an automated backup client that generates a local JSON report and uploads it to a remote storage endpoint via Multipart Form-Data.
3. Step A (Generate Local File):
   - Create a dictionary named 'backup_report' containing simulated pipeline metrics:
     {"timestamp": "2026-07-26", "status": "SUCCESS", "records_processed": 5000, "errors": 0}
   - Define a local filepath: filepath = "pipeline_report.json"
   - Use 'with open(filepath, "w", encoding="utf-8") as f:' and 'json.dump(backup_report, f, indent=4)' to save the file to disk.
4. Step B (Prepare Multipart Payload):
   - Target URL: url = "https://httpbin.org/post"
   - Open the newly generated file in BINARY READ mode ('with open(filepath, "rb") as file_to_upload:').
   - Create the files dictionary: files_payload = {"file": ("pipeline_report.json", file_to_upload, "application/json")}
     (Note: Passing a tuple (filename, file_object, content_type) is the enterprise standard for multipart uploads!).
   - Create a standard form-data dictionary to accompany the file: form_data = {"project": "PythonCore", "environment": "Production"}
5. Step C (Execute Upload):
   - Inside the same 'with' block, make a POST request to 'url' passing 'files=files_payload', 'data=form_data', and 'timeout=10'.
   - Verify the upload succeeded using '.raise_for_status()'.
6. Step D (Verification & Reporting):
   - Parse the JSON returned by httpbin.org.
   - Verify and print:
     1. The standard form data received by the server (inside the 'form' key).
     2. The exact file content string echoed back by the server (inside the 'files' -> 'file' key).
7. Step E (Cleanup):
   - In a 'finally' block (or after execution), delete 'pipeline_report.json' from disk using 'os.remove()' to leave the environment clean!
"""

import requests, json, os

local_json_file = os.path.join(os.path.dirname(__file__), "backup_report.json")
json_dict = {
    "timestamp": "2026-07-26", 
    "status": "SUCCESS", 
    "records_processed": 5000, 
    "errors": 0
   }
base_url = "https://httpbin.org/post"
with open(local_json_file, "w") as json_file:
   json.dump(json_dict, json_file, indent=4)
with open(local_json_file, "rb") as file_to_upload:
   files_payload = {"file": ("pipeline_report.json", file_to_upload, "application/json")}
   form_data = {"project": "PythonCore", "environment": "Production"}
   try:
      response = requests.post(base_url, files=files_payload,data=form_data, timeout=10)
      response.raise_for_status()
      data_json = response.json()
      print(data_json['form'])
      print(data_json['files']['file'])
   except requests.exceptions.RequestException as e:
      print(f"[ERROR] {e}.")
   except Exception as e:
      print(f"[ERROR] {e}.")
   finally:
      if os.path.exists(local_json_file):
        os.remove(local_json_file)
        print("\nTemporary upload file cleaned up from disk.")
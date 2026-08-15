"""
Python Core - 06 Libraries (requests)
Exercise 18: The Distributed Fault-Tolerant Backup & Multipart Pipeline (Hardcore - Full Ecosystem Integration)
Folder: 18_fault_tolerant_backup_pipeline/
Main File: main.py

Scenario:
You are tasked with building a disaster-recovery agent. The agent must download a compressed binary database backup from a remote server using chunked streaming, calculate its integrity metrics, generate an audit JSON manifest on disk, and upload both the binary backup AND the JSON manifest simultaneously via a Multipart Form-Data request to a secure vault — all while protected by connection pooling and retry algorithms.

Rules:
1. Import 'requests', 'json', 'os', 'HTTPAdapter' from 'requests.adapters', and 'Retry' from 'urllib3.util.retry'.
2. Step A (Resilient Infrastructure):
   - Build a 'requests.Session()' equipped with a 3-retry backoff HTTPAdapter (for 429 and 5xx errors) mounted to HTTP/HTTPS.
   - Define local filepaths: bin_filepath = "db_backup.bin" and manifest_filepath = "audit_manifest.json".
3. Step B (Resilient Chunked Download):
   - Download a binary payload from url_source = "https://httpbin.org/bytes/150000" (150 KB) using 'stream=True' and Context Manager.
   - Iterate using 'iter_content(chunk_size=16384)' (16 KB chunks) and save to 'bin_filepath' in binary write mode ('wb').
   - Track the total downloaded bytes in a variable.
4. Step C (Manifest Generation):
   - Check the physical file size on disk using 'os.path.getsize(bin_filepath)' and verify it matches your byte counter.
   - Create a Python dictionary 'manifest_data':
     {"job_id": "VALKYRIE-09", "timestamp": "2026-07-27", "file_name": "db_backup.bin", "size_bytes": actual_size, "integrity_check": "PASSED"}
   - Save this dictionary to 'manifest_filepath' using 'json.dump(..., indent=4)'.
5. Step D (Simultaneous Multipart Vault Upload):
   - Target vault URL: vault_url = "https://httpbin.org/post"
   - You must upload BOTH files in a single HTTP request!
   - Open 'bin_filepath' in 'rb' mode AND open 'manifest_filepath' in 'rb' mode simultaneously using nested or comma-separated Context Managers:
     'with open(bin_filepath, "rb") as f_bin, open(manifest_filepath, "rb") as f_man:'
   - Build the multipart files dictionary passing standard enterprise 3-tuples:
     files_payload = {
         "database_binary": ("db_backup.bin", f_bin, "application/octet-stream"),
         "audit_manifest": ("audit_manifest.json", f_man, "application/json")
     }
   - Send standard form data alongside: data_payload = {"vault_tier": "GLACIER_DEEP_ARCHIVE", "retention_years": "7"}
   - Execute the POST request via your resilient session with 'timeout=15' and call '.raise_for_status()'.
6. Step E (Audit Verification & Automated Cleanup):
   - Parse the JSON response from httpbin.org.
   - Verify and print to terminal:
     1. The form metadata received ('form' key).
     2. The proof that BOTH files were received by the server ('files' key showing keys for both 'database_binary' and 'audit_manifest').
   - In the 'finally' block, ensure the session is closed AND both local files ('db_backup.bin' and 'audit_manifest.json') are safely deleted from disk using 'os.remove()' after checking 'os.path.exists()'.
"""

import requests, json, os
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3 import Retry

retry_strategy = Retry(
    total =3,
    backoff_factor=0.5,
    status_forcelist=[429,500,502,503,504],
    allowed_methods=["GET", "POST"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)

bin_filepath = os.path.join(os.path.dirname(__file__), "db_backup.bin")
manifest_filepath = os.path.join(os.path.dirname(__file__), "audit_manifest.json")
url_source = "https://httpbin.org/bytes/150000"
total_bytes = 0
vault_url = "https://httpbin.org/post"

try:
   with session.get(url_source, stream = True, timeout = 10) as response:
      response.raise_for_status()
      with open(bin_filepath,"wb") as file:
        for line in response.iter_content(chunk_size=16384):
            if line:
              total_bytes +=len(line)
              file.write(line)
      if os.path.getsize(bin_filepath) == total_bytes:
         date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         manifest_data = {
            "job_id": "VALKYRIE-09",
            "timestamp": date,
            "file_name": "db_backup.bin",
            "size_bytes": total_bytes,
            "integrity_check": "PASSED"
         }
         with open(manifest_filepath, "w") as json_file:
            json.dump(manifest_data, json_file, indent=4)
         with open(bin_filepath, "rb") as f_bin, open(manifest_filepath, "rb") as f_man:
            files_payload = {
                "database_binary": ("db_backup.bin",f_bin,"application/octet-stream"),
                "audit_manifest": ("audit_manifest.json",f_man,"application/json")
                }
            data_payload = {
                "vault_tier": "GLACIER_DEEP_ARCHIVE",
                "retention_years": "7"
                }
            response = session.post(vault_url, files=files_payload, data=data_payload, timeout=15)
            response.raise_for_status()
            data_json = response.json()
            print(f"\nForm metadata received: {data_json['form']}"
                  f"\nProof that BOTH files were received by the server: {data_json['files']}")
            
except requests.exceptions.RequestException as e:
   print(f"[ERROR] {e}.") 
except Exception as e:
   print(f"[ERROR] {e}.")    
finally:
   session.close()
   if os.path.exists(bin_filepath):
      os.remove(bin_filepath)
   if os.path.exists(manifest_filepath):
      os.remove(manifest_filepath)

"""
Python Core - 06 Libraries (requests)
Exercise 16: The Resilient Streaming ETL Engine (Hardcore - Architecture & Integration)
Folder: 16_resilient_streaming_etl/
Main File: main.py

Scenario:
You are building an Extract, Transform, and Load (ETL) data pipeline. You must extract a continuous stream of raw records from a fragile data source, transform the data on the fly without using disk storage, and load (POST) the cleaned data in batches to a destination API.

Rules:
1. Import 'requests', 'json', 'HTTPAdapter' from 'requests.adapters', and 'Retry' from 'urllib3.util.retry'.
2. Step A (Engine Resilience & Session Setup):
   - Configure a 'Retry' strategy: total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET", "POST"].
   - Create a single persistent 'requests.Session()' and mount the adapter to both HTTP and HTTPS.
   - Set custom global headers: {"User-Agent": "HardcoreETLEngine/1.0", "Accept": "application/json"}.
3. Step B (Extract - Streaming Ingestion):
   - Target source URL: source_url = "https://httpbin.org/stream/20" (Streams 20 JSON lines).
   - Use a Context Manager ('with session.get(...) as response:') with 'stream=True' and 'timeout=10'.
   - Iterate through the data line-by-line using 'response.iter_lines(decode_unicode=True)'.
4. Step C (Transform - On-The-Fly Processing):
   - For each valid line extracted, parse the string into a Python dictionary using 'json.loads(line)'.
   - Extract only the 'id' (or loop index if id is missing) and the 'headers' dictionary from the raw payload.
   - Create a cleaned dictionary: {"record_id": index, "source_ip": raw_dict.get("origin"), "status": "PROCESSED"}.
   - Append this cleaned record to an in-memory list called 'batch_payload'.
5. Step D (Load - Batch POSTing):
   - To avoid network congestion, whenever 'batch_payload' reaches exactly 5 records, send a POST request to:
     destination_url = "https://httpbin.org/post"
   - Send the batch using 'json={"batch": batch_payload}' via your resilient session.
   - Verify the POST succeeded (status code 200), print a log: "[ETL LOAD] Successfully dispatched batch of 5 records!", and clear the 'batch_payload' list to free up RAM.
6. Step E (Flush Remaining & Final Report):
   - After the stream ends, if there are any remaining records in 'batch_payload', POST them as a final batch.
   - Print a complete summary showing total raw records extracted, total batches dispatched, and confirm zero-disk footprint execution.
   - Always close the session in a finally block!
"""

import requests, json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

source_url = "https://httpbin.org/stream/20"
destination_url = "https://httpbin.org/post"
batch_payload = []
total_records = 0
total_batches = 0
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
session.headers.update({
    "User-Agent": "HardcoreETLEngine/1.0", 
    "Accept": "application/json"
    })

try:
   with session.get(source_url, stream=True, timeout=10) as response:
      response.raise_for_status()
      for i,line in enumerate(response.iter_lines(decode_unicode=True)):
         if line:
            data = json.loads(line)
            raw_dict = {
               "record_id": data.get("id",i),
               "source_ip": data.get("origin"),
               "status": "PROCESSED"
            }
            print(json.dumps(raw_dict,indent=4))
            total_records +=1
            batch_payload.append(raw_dict)
            if len(batch_payload) == 5:
               post_response = session.post(destination_url, json={"batch": batch_payload}, timeout=5)
               post_response.raise_for_status()
               print("[ETL LOAD] Successfully dispatched batch of 5 records!")
               total_batches +=1
               batch_payload.clear()
except requests.exceptions.RequestException as e:
   print(f"[ERROR] {e}.")
except Exception as a:
   print(f"[ERROR] {a}.")
finally:
   if batch_payload:
      post_response = session.post(destination_url, json={"batch": batch_payload}, timeout=5)
      post_response.raise_for_status()
      total_batches +=1
      batch_payload.clear()
   print(f"""
   ===== ETL FINAL REPORT =====
   Total raw records extracted: {total_records}
   Total batches dispatched: {total_batches}
   Execution mode: Zero-disk footprint confirmed
   ============================
   """)
   session.close()
"""
Python Core - 06 Libraries (requests)
Exercise 12: The Resilient Big Data Pipeline (Hard - Architecture & Integration)
Folder: 12_resilient_big_data_pipeline/
Main File: main.py

Rules:
1. Import 'requests', 'time', 'HTTPAdapter' from 'requests.adapters', and 'Retry' from 'urllib3.util.retry'.
2. Real-world Data Engineering Challenge: You must ingest a continuous stream of records from an unstable API.
   You cannot save the file to disk; you must process the chunks ON THE FLY in memory while protected against network blips!
3. Step A (Resilience Setup):
   - Configure a 'Retry' strategy with 'total=3', 'backoff_factor=0.5', and attach it to a new 'Session' via an 'HTTPAdapter'.
   - Set a custom User-Agent in the session headers: "ResilientDataPipeline/1.0".
4. Step B (Streaming Ingestion Setup):
   - We will use httpbin's stream endpoint, which streams JSON lines: url = "https://httpbin.org/stream/50" (Streams 50 JSON lines).
   - Initialize two counter variables: 'lines_processed = 0' and 'total_bytes_received = 0'.
5. Step C (Execution & On-The-Fly Processing):
   - Use a Context Manager to open the session GET request with 'stream=True' and 'timeout=10'.
   - Verify the request succeeded with '.raise_for_status()'.
   - Instead of iterating by byte chunks, use 'response.iter_lines(decode_unicode=True)' to stream the payload line by line!
6. Step D (Data Transformation):
   - For each line yielded by 'iter_lines()':
     a) Check if the line is not empty.
     b) Increment your 'lines_processed' counter by 1.
     c) Add the length of the string ('len(line)') to 'total_bytes_received'.
     d) To simulate heavy data processing without cluttering the screen, only print a progress log every 10 lines:
        f"[PIPELINE LOG] Ingested line {lines_processed}... (Current stream buffer: {total_bytes_received} bytes)"
7. Step E (Final Reporting):
   - Catch 'requests.exceptions.RequestException' to gracefully report any network failures.
   - Print a final pipeline execution summary:
     "=== Pipeline Execution Summary ==="
     "Total Records Ingested: X lines"
     "Total Payload Processed: Y bytes"
     "Status: Zero-disk footprint ingestion completed successfully under retry protection!"
8. Close the session properly!
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total = 3,
    backoff_factor= 0.5,
    status_forcelist=[429,500,502,503,504],
    allowed_methods=["GET"],
    raise_on_status=True
)

adapter = HTTPAdapter(max_retries=retry_strategy)
url = "https://httpbin.org/stream/50"
lines_processed = 0
total_bytes_received = 0
session = requests.Session()
session.mount("http://",adapter)
session.mount("https://", adapter)
session.headers.update({
    "User-Agent": "ResilientDataPipeline/1.0"
})
success = False
try:
   with session.get(url, stream=True, timeout=10) as response:   
      response.raise_for_status()
      for line in response.iter_lines(decode_unicode=True):
         if line:
            lines_processed += 1
            total_bytes_received += len(line)
         if lines_processed % 10 == 0:
            print(f"[PIPELINE LOG] Ingested line {lines_processed}... (Current stream buffer: {total_bytes_received} bytes)")
      success = True
except requests.exceptions.RequestException as e:
   print(f"[ERROR]: {e}.")   
finally:
   print("=== Pipeline Execution Summary ===\n"
         f"Total Records Ingested: {lines_processed} lines\n"
         f"Total Payload Processed: {total_bytes_received} bytes"
      )
   if success == True:
      print("Status: Zero-disk footprint ingestion completed successfully under retry protection!")
   else:
      print("Status: Failed.")
   session.close() 
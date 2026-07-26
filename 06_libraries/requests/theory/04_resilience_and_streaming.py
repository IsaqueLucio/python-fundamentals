"""
Python Core - 06 Libraries
Module: requests
File: 04_resilience_and_streaming.py
Description: Mastering automatic retries with HTTPAdapters, handling rate limits, and downloading big data in streams.
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

print("--- 1. Building a Resilient Session (Automatic Retries) ---")
# Instead of manually writing try/except loops to retry when a server drops,
# we configure urllib3's Retry engine and mount it to a requests Session!

# Configure the retry strategy:
retry_strategy = Retry(
    total=3,  # Maximum number of retry attempts
    backoff_factor=1,  # Wait times: {backoff factor} * (2 ** ({number of total retries} - 1)) -> 1s, 2s, 4s...
    status_forcelist=[429, 500, 502, 503, 504],  # Status codes to automatically retry
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # Only retry safe, idempotent HTTP methods
)

# Create an HTTPAdapter with this strategy:
adapter = HTTPAdapter(max_retries=retry_strategy)

# Mount the adapter to a new Session for both HTTP and HTTPS:
resilient_session = requests.Session()
resilient_session.mount("http://", adapter)
resilient_session.mount("https://", adapter)

url_unstable = "https://httpbin.org/status/503"  # Always returns 503 Service Unavailable

print("Attempting to hit an unstable endpoint (503). Watch the engine retry automatically...")
try:
    # Notice: we just call .get() normally. The Session + Adapter handles the waiting and retries in the background!
    response = resilient_session.get(url_unstable, timeout=5)
    response.raise_for_status()
except requests.exceptions.RetryError as e:
    print(f"[RESILIENCE REPORT] Max retries exceeded! The server is truly down: {e}")
except requests.exceptions.RequestException as e:
    print(f"[REQUEST ERROR] {e}")

resilient_session.close()
print("\n" + "="*60 + "\n")


print("--- 2. Streaming Big Data (Downloading in Chunks) ---")
# To download a large file without consuming GBs of RAM, we MUST pass 'stream=True'.
# This delays downloading the body until we explicitly iterate through it!

# Let's download a sample image (or a large binary payload from httpbin):
url_big_data = "https://httpbin.org/bytes/50000"  # Generates a 50,000-byte binary file
output_filepath = "streamed_backup.bin"

print("Starting streamed download...")
try:
    # Notice: stream=True tells requests: "Only download the headers for now!"
    with requests.get(url_big_data, stream=True, timeout=10) as stream_res:
        stream_res.raise_for_status()
        
        # Check total file size from headers (if the server provides it):
        total_size = stream_res.headers.get('content-length')
        print(f"Server reported file size: {total_size} bytes")
        
        # Open local file in binary write mode ('wb'):
        with open(output_filepath, "wb") as file:
            # We download and save in chunks of 8192 bytes (8 KB) at a time:
            for chunk in stream_res.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive new chunks
                    file.write(chunk)
                    
    print(f"[SUCCESS] File saved successfully! Local disk size: {os.path.getsize(output_filepath)} bytes.")

except requests.exceptions.RequestException as e:
    print(f"[STREAM ERROR] Failed to download file: {e}")

finally:
    # Clean up the generated test file from disk:
    if os.path.exists(output_filepath):
        os.remove(output_filepath)
        print("Test file cleaned up from disk.")
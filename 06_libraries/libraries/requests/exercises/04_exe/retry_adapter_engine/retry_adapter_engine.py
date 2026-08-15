"""
Python Core - 06 Libraries (requests)
Exercise 11: The Retry Adapter Engine (Intermediate - Logic & Interpretation)
Folder: 11_retry_adapter_engine/
Main File: main.py

Rules:
1. Import 'requests', 'HTTPAdapter' from 'requests.adapters', and 'Retry' from 'urllib3.util.retry'.
2. You are building a fault-tolerant HTTP client for a production environment.
3. Configure a 'Retry' object named 'retry_strategy' with the following rules:
   - 'total=3' (Try 3 times before giving up).
   - 'backoff_factor=1' (Wait 1s, then 2s, then 4s between retries).
   - 'status_forcelist=[429, 500, 502, 503, 504]' (Retry on rate limits and server crashes).
   - 'allowed_methods=["GET"]'.
4. Create an 'HTTPAdapter' passing your 'retry_strategy'.
5. Instantiate a 'requests.Session()' and use '.mount("https://", adapter)' to attach your engine to all HTTPS requests.
6. Define a target URL that we KNOW will fail with a server error: url = "https://httpbin.org/status/503"
7. Use a 'try/except' block to execute 'session.get(url, timeout=5)'.
8. Watch the terminal during execution! You should notice the script pausing automatically as it executes the backoff retries.
9. Catch 'requests.exceptions.RetryError' specifically, and print:
   "[FAULT TOLERANCE] Engine exhausted all 3 retry attempts! Server is unreachable."
10. Ensure you close the session at the end of your script!
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total = 3,
    backoff_factor=1,
    status_forcelist=[429,500,502,503,504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://",adapter)
session.mount("https://", adapter)
url = "https://httpbin.org/status/503"

try:
    res = session.get(url, timeout=5)
    res.raise_for_status()
except requests.exceptions.RetryError as e:
    print("[FAULT TOLERANCE]: Engine exhausted all 3 retry attempts! Server is unreachable.")
except requests.exceptions.RequestException as e:
    print(f"[ERROR]: {e}.")
finally:
    session.close()
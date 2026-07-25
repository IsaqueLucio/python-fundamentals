"""
Python Core - 06 Libraries (requests)
Exercise 8: The Session Benchmark (Intermediate - Logic & Interpretation)
Folder: 08_session_benchmark/
Main File: main.py

Rules:
1. Import 'requests' and 'time'.
2. Define a target URL that responds quickly: test_url = "https://httpbin.org/get"
3. Define a constant for the number of requests: REQUEST_COUNT = 10
4. Part 1 (Standalone Loop):
   - Record the start time using 'time.time()'.
   - Create a loop that executes 'requests.get(test_url, timeout=5)' exactly REQUEST_COUNT times.
   - Calculate and print the total execution time for the standalone requests.
5. Part 2 (Session Context Manager):
   - Record a new start time.
   - Use a Context Manager ('with requests.Session() as session:') to open a persistent connection pool.
   - Inside the 'with' block, create a loop that executes 'session.get(test_url, timeout=5)' exactly REQUEST_COUNT times.
   - Calculate and print the total execution time for the session requests.
6. Mathematical Comparison:
   - Calculate the percentage speedup using the formula: 
     speedup = ((standalone_time - session_time) / standalone_time) * 100
   - Print a clean summary report showing both times and the exact percentage of time saved by reusing the TCP/IP connection!
"""

import requests
import time

test_url = "https://httpbin.org/get"
REQUEST_COUNT = 1000

print(f"Executing {REQUEST_COUNT} requests using standalone requests.get() (No connection reuse)...")
start_time = time.time()
for _ in range(REQUEST_COUNT):
   try:
      print(f"{_}nd/{REQUEST_COUNT} lap of the loop.")
      res1 = requests.get(test_url, timeout=5)
      res1.raise_for_status()
   except requests.exceptions.RequestException as e:
      print(f"[ERROR] Occurred on the {_}/{REQUEST_COUNT} iteration of the loop: {e}")
standalone_time = time.time() - start_time
print(f"Standalone total time: {standalone_time:.4f} seconds")

print(f"\nExecuting {REQUEST_COUNT} requests using requests.Session() (Connection pooling)...")
start_time = time.time()
with requests.Session() as session:
   for _ in range(REQUEST_COUNT):
      try:
         print(f"{_}nd/{REQUEST_COUNT} lap of the loop.")
         res2 = session.get(test_url, timeout=5)
         res2.raise_for_status()
      except requests.exceptions.RequestException as e:
         print(f"[ERROR] Occurred on the {_}/{REQUEST_COUNT} iteration of the loop: {e}")
session_time = time.time() - start_time
print(f"Session total time:    {session_time:.4f} seconds")

if standalone_time > 0 and session_time > 0:
    speedup = ((standalone_time - session_time) / standalone_time) * 100
    print(f"\n[PERFORMANCE WIN] Session was {speedup:.1f}% faster!")

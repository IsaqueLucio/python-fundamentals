"""
Python Core - 06 Libraries
Module: requests
File: 03_sessions_and_cookies.py
Description: Understanding connection pooling, shared headers, cookie persistence, and performance benchmarking.
"""
import requests
import time

print("--- 1. Shared Headers and Auth Across Requests ---")
# Instead of calling requests.get(), we instantiate a Session object:
session = requests.Session()

# Set headers ONCE for the entire lifecycle of this session:
session.headers.update({
    "User-Agent": "PythonCore-DeepDive-SessionEngine/2.0",
    "Accept": "application/json"
})

# All requests made through 'session' now inherit these headers automatically!
url_headers = "https://httpbin.org/headers"
try:
    res1 = session.get(url_headers, timeout=5)
    print("First Request User-Agent sent:")
    print(res1.json()["headers"]["User-Agent"])
except requests.exceptions.RequestException as e:
    print(f"[ERROR] {e}")

print("\n" + "="*60 + "\n")


print("--- 2. Automatic Cookie Persistence (Stateful Navigation) ---")
# When you log into a website, the server gives you a Session Cookie.
# Standalone requests.get() throws cookies away. requests.Session() saves them!

# Step A: Hit an endpoint that sets a cookie named 'session_token' with value 'xyz_123'
url_set_cookie = "https://httpbin.org/cookies/set/session_token/xyz_123"
session.get(url_set_cookie, timeout=5)

# Step B: Check our saved cookies without sending anything explicitly!
url_check_cookies = "https://httpbin.org/cookies"
res_cookies = session.get(url_check_cookies, timeout=5)

print("Cookies automatically stored and resent by the Session:")
print(res_cookies.json())

print("\n" + "="*60 + "\n")


print("--- 3. Performance Benchmark: Standalone vs Session ---")
# Let's prove the speed difference by making 5 consecutive requests to the same server.
TEST_URL = "https://httpbin.org/get"
RUNS = 5

print(f"Executing {RUNS} requests using standalone requests.get() (No connection reuse)...")
start_time = time.time()
for _ in range(RUNS):
    try:
        requests.get(TEST_URL, timeout=5)
    except requests.exceptions.RequestException:
        pass
standalone_time = time.time() - start_time
print(f"Standalone total time: {standalone_time:.4f} seconds")

print(f"\nExecuting {RUNS} requests using requests.Session() (Connection pooling)...")
start_time = time.time()
for _ in range(RUNS):
    try:
        session.get(TEST_URL, timeout=5)
    except requests.exceptions.RequestException:
        pass
session_time = time.time() - start_time
print(f"Session total time:    {session_time:.4f} seconds")

# Calculate percentage speedup
if standalone_time > 0 and session_time > 0:
    speedup = ((standalone_time - session_time) / standalone_time) * 100
    print(f"\n[PERFORMANCE WIN] Session was {speedup:.1f}% faster!")

# Always close the session when done (or use it inside a Context Manager: 'with requests.Session() as s:')
session.close()
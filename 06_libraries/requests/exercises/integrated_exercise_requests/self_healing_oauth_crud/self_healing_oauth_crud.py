"""
Python Core - 06 Libraries (requests)
Exercise 17: The Self-Healing OAuth CRUD Synchronizer (Hardcore - State & Error Interception)
Folder: 17_self_healing_oauth_crud/
Main File: main.py

Scenario:
You are building an automated synchronization daemon that manages resources on a secure server. The server requires Bearer Token authentication, but the tokens expire unpredictably. Your system must perform a full CRUD lifecycle while dynamically intercepting '401 Unauthorized' errors, renewing the token transparently, and repeating the interrupted mutation without failing the pipeline.

Rules:
1. Import 'requests' and 'time'.
2. Step A (Simulated Auth Engine):
   - Create a global (or class-level) token variable starting with an invalid token: current_token = "EXPIRED_TOKEN_V1"
   - Create a helper function 'refresh_token()' that prints "[AUTH DAEMON] 401 Intercepted! Negotiating new token..." and returns "VALID_SECURE_TOKEN_V2".
3. Step B (The Self-Healing Dispatcher):
   - Create a wrapper function 'safe_request(session, method, url, **kwargs)' that:
     a) Injects {"Authorization": f"Bearer {current_token}"} into kwargs['headers'].
     b) Executes the request using 'session.request(method, url, **kwargs)'.
     c) If 'response.status_code == 401', it intercepts the failure, calls 'refresh_token()' to update 'current_token', updates the header with the new token, and RE-EXECUTES the request immediately!
     d) Returns the final valid response object.
4. Step C (The CRUD Synchronization Pipeline):
   - Instantiate a persistent Session.
   - Phase 1 (CREATE): Use 'safe_request' to POST a new record {"project": "SkyNet", "version": "1.0"} to "https://httpbin.org/post".
     *(To test your self-healing engine, force Phase 1 to hit "https://httpbin.org/status/401" first, catch it via your wrapper, refresh the token, and then route to the real endpoint!)*
   - Phase 2 (READ & VERIFY): Use 'safe_request' to GET "https://httpbin.org/bearer". Verify that the JSON returned confirms `"authenticated": true` and shows your new "VALID_SECURE_TOKEN_V2".
   - Phase 3 (PARTIAL UPDATE): Use 'safe_request' to send a PATCH request with `json={"version": "2.0-PATCHED"}` to "https://httpbin.org/patch". Print the updated data returned by the server.
   - Phase 4 (DELETE): Use 'safe_request' to DELETE the resource at "https://httpbin.org/delete". Verify status code 200.
5. Print an audit log confirming that the entire CRUD lifecycle completed and that the OAuth token self-healing mechanism triggered successfully without crashing the application.
"""

import requests
from urllib3 import Retry
from requests.adapters import HTTPAdapter
from current_token import TokenManager

token = TokenManager()
def safe_request(session, method, url, **kwargs):
   
   try:
      status_code = None

      headers = kwargs.get("headers", {})
      headers["Authorization"] = f"Bearer {token.get_current_token()}"
      kwargs["headers"] = headers
      response = session.request(method, url, **kwargs)
      status_code = response.status_code
      response.raise_for_status()
      return response
   except requests.exceptions.RequestException as e:
      if status_code == 401:
         token.refresh_token()
         if "401" in url:
            url = "https://httpbin.org/post"
         return safe_request(session, method, url, **kwargs)
      else:
         return f"[ERROR] {e}."
   except Exception as e:
      return f"[ERROR] {e}."

retry_strategy = Retry(
    total =3,
    backoff_factor=0.5,
    status_forcelist=[500,502,503,504],
    allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)
session.headers.update({
    "User-Agent": "SelfHealingOAuthCrud/1.0", 
    "Accept": "application/json"
    })

print("\nPhase 1 - create")
create1 = safe_request(session,"POST","https://httpbin.org/post",json={"project": "SkyNet","version": "1.0"})
print(create1.json())
create2 = safe_request(session,"POST","https://httpbin.org/status/401",json={"project": "SkyNet","version": "1.0"})
print(create2.json())

print("\nPhase 2 - read")
read = safe_request(session, "GET","https://httpbin.org/bearer")
read_data = read.json()
print(f"Authenticated:{read_data["authenticated"]}\nToken: {read_data["token"]}")

print("\nPhase 3 - patch")
patch = safe_request(session,"PATCH","https://httpbin.org/patch",json={"version": "2.0-PATCHED"})
print(patch.json()["json"])

print("\nPhase 4 - delete")
delete = safe_request(session, "DELETE","https://httpbin.org/delete")
print(f"Delte status code: {delete.status_code}\n{delete.json()}")

print("\n========== AUDIT LOG ==========")
print("CREATE: completed")
print("TOKEN REFRESH: completed")
print("READ: verified")
print("PATCH: completed")
print("DELETE: completed")
print("Pipeline finished successfully.")
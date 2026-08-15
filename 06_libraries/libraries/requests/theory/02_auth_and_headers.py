"""
Python Core - 06 Libraries
Module: requests
File: 02_auth_and_headers.py
Description: Mastering custom headers, User-Agents, Bearer Tokens, Basic Auth, and auth status codes.
"""
import requests
from requests.auth import HTTPBasicAuth

print("--- 1. Custom Headers and Disguising Your Script (User-Agent) ---")
# By default, Python sends 'User-Agent: python-requests/x.x.x'.
# Many servers block this! We must disguise our script as a legitimate web browser.

url_headers = "https://httpbin.org/headers"

# Custom headers dictionary
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8",
    "X-Custom-Client-App": "PythonCore-DeepDive/1.0"
}

response = requests.get(url_headers, headers=custom_headers, timeout=5)
print(f"Status Code: {response.status_code}")
print("Headers echoed back by the server:")
response.raise_for_status()
print(response.json()["headers"])
print("\n" + "="*60 + "\n")


print("--- 2. Authentication via Bearer Token (API Keys in Headers) ---")
# The modern standard for REST APIs is sending a secret token inside the Authorization header.
# Format: {"Authorization": "Bearer <your_token>"}

url_bearer = "https://httpbin.org/bearer"
my_secret_token = "super_secret_jwt_token_12345"

auth_headers = {
    "Authorization": f"Bearer {my_secret_token}",
    "Content-Type": "application/json"
}

try:
    res_token = requests.get(url_bearer, headers=auth_headers, timeout=5)
    res_token.raise_for_status()
    
    data = res_token.json()
    print("Token Auth Successful!")
    print(f"Authenticated: {data['authenticated']}")
    print(f"Token received by server: {data['token']}")
except requests.exceptions.HTTPError as e:
    print(f"[AUTH ERROR] Failed to authenticate: {e}")

print("\n" + "="*60 + "\n")


print("--- 3. HTTP Basic Authentication (Username & Password) ---")
# Some legacy systems or internal tools require traditional Basic Auth.
# requests provides a clean shorthand: auth=('user', 'pass') or auth=HTTPBasicAuth('user', 'pass')

url_basic_auth = "https://httpbin.org/basic-auth/admin/secret123"

# Let's test with correct credentials
res_auth_ok = requests.get(url_basic_auth, auth=("admin", "secret123"), timeout=5)
print(f"Correct credentials status: {res_auth_ok.status_code} (Success)")
print(res_auth_ok.json())

# Let's test with WRONG credentials to trigger an error
res_auth_fail = requests.get(url_basic_auth, auth=("admin", "wrong_password"), timeout=5)
print(f"Wrong credentials status:   {res_auth_fail.status_code} (Unauthorized)")

print("\n" + "="*60 + "\n")


print("--- 4. Understanding Status Codes 401 vs 403 ---")
# It is vital for a software engineer to know the exact difference between these two:
# 401 Unauthorized: "I don't know who you are. Provide valid credentials/tokens."
# 403 Forbidden:    "I know EXACTLY who you are, but you do not have permission to see this."

print("401 = Who are you? (Unauthenticated)")
print("403 = You can't enter here! (Unauthorized/No Permissions)")
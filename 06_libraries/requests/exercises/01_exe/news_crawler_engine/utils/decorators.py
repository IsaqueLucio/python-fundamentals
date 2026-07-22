"""
Python Core - 06 Libraries
Module: requests
Exercise 03: News Crawler Engine (Hard)
File: decorators.py

Rules:
1. Import 'requests' and 'functools' (optional, for @wraps).
2. Create a decorator called 'network_monitor(func)'.
3. The wrapper function should execute the original function inside a 'try/except' block.
4. Catch 'requests.exceptions.RequestException' (which covers network errors, timeouts, and HTTP errors).
5. If an exception occurs, print "[NETWORK FAILURE] Unable to reach the external server." and return None instead of crashing the application.
"""

import requests, functools

def network_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args,**kwargs)
            return result
        except requests.exceptions.RequestException as e:
            print(f"[NETWORK FAILURE] Unable to reach the external server: {e}.")
            return None
    return wrapper
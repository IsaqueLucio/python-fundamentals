"""
Exercise 3: The Retry Mechanism
Main File: main.py

Rules:
1. Create a decorator called 'retry_three_times(func)'.
2. Inside its wrapper:
   - Create a loop that runs up to 3 times (e.g., for attempt in range(1, 4):).
   - Inside the loop, use a 'try' block to call the original function and return its result immediately if it succeeds.
   - If it raises an Exception, catch it in an 'except Exception as e' block and print:
     f"[WARNING] Attempt {attempt} failed with error: '{e}'. Retrying..."
   - If the loop finishes all 3 attempts without success, print:
     "[ERROR] Function failed after 3 attempts." and return None.
3. Create a function 'unstable_network_request()' that explicitly raises a ConnectionError:
   raise ConnectionError("Timeout connecting to server!")
4. Apply @retry_three_times to 'unstable_network_request()' and call it to watch the resilience loop in action!
"""

from retry_mechanism import retry_three_times

@retry_three_times
def unstable_network_request():
    raise ConnectionError("Timeout connecting to server!")

unstable_network_request()

@retry_three_times
def soma(a, b):
    return a + b

print(soma(5, 8))
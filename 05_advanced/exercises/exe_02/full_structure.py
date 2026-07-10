"""
Exercise 3: Full Try/Except/Else/Finally
Main File: main.py

Rules:
1. Create a function 'simulate_api_request(server_status: str)'.
2. Inside the function, write the full 'try/except/else/finally' block structure.
3. In the 'try' block:
   - If 'server_status' is "offline", forcefully raise a ConnectionError: raise ConnectionError("Server is down!")
   - Else, create a variable 'data = "User JSON Data"'.
4. In the 'except ConnectionError as e' block:
   - Print: f"Failed to connect: {e}"
5. In the 'else' block (runs only if NO exception occurred in the try block):
   - Print: f"Data retrieved successfully: {data}"
6. In the 'finally' block (runs always):
   - Print: "Closing API session. Memory cleared.\\n"
7. OUTSIDE the function, test the code by calling:
   - simulate_api_request("online")
   - simulate_api_request("offline")
"""

def simulate_api_request(server_status: str):
    try:
        server_status = server_status.lower()
        if server_status == "offline":
            raise ConnectionError("Server is down!")
        elif server_status == "online":
            data = "User JSON Data"
    except ConnectionError as e:
        print(f"Failed to connect: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Data retrieved successfully: {data}")
    finally:
        print("Closing API session. Memory cleared.\\n")
    
simulate_api_request("Online")
simulate_api_request("OFFline")
simulate_api_request(10)
simulate_api_request("test")
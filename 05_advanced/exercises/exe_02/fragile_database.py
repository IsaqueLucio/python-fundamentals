"""
Exercise 2: Fragile Database
Main File: main.py

Rules:
1. Create a dictionary: user_db = {"alice": "Admin", "bob": "User"}
2. Create a list: servers = ["Server_A", "Server_B"]
3. Write a 'try' block. 
   - Inside it, try to print the value of a non-existent key (e.g., user_db["charlie"]).
   - Also inside it, try to print the 5th element of the servers list (e.g., servers[5]).
4. Catch the 'KeyError' and print: "CRITICAL: User not found in the database."
5. Catch the 'IndexError' and print: "CRITICAL: Server index out of range."
6. Run the code. Notice which error is caught first and how the 'try' block execution stops immediately when an error occurs!
"""

user_db = {"alice": "Admin", "bob": "User"}
servers = ["Server_A", "Server_B"]

try:
    print(f"{user_db["charlie"]}")
    print(f"{servers[5]}")
except KeyError:
    print("CRITICAL: User not found in the database.")
except IndexError:
    print("CRITICAL: Server index out of range.")
    
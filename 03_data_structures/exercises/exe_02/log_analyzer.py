"""
Exercise 2: Log Analyzer
File: 05_log_analyzer.py

Rules:
1. Create a tuple representing a sequence of HTTP status codes from a server log:
   logs = (200, 404, 200, 500, 200, 403, 200, 404)
2. Use the .count() method to find out how many times the '200' success code appears and print the result.
3. Use the .index() method to find the exact position of the first '500' error and print the result.
4. Attempt to change the first item of the tuple (e.g., logs[0] = 201).
5. Run the code, observe the TypeError, and then COMMENT OUT that line to fix the script. 
   Leave a comment next to it explaining why it failed.
"""

logs = (200, 404, 200, 500, 200, 403, 200, 404)
success_count = logs.count(200)
print(f"The code 200 appeared {success_count} times.")

error_position = logs.index(500)
print(f"The first 500 error was found at index {error_position}.")

#logs[0] = 201 | tuple objects does not support item assignment

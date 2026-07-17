"""
Exercise 2: Large Log File Streamer
Main File: main.py

Rules:
1. Create a list simulating a large log file in memory (just for our mock):
   mock_log_file = [
       "INFO: User Isaque logged in",
       "ERROR: Database connection failed",
       "INFO: Page rendered successfully",
       "WARNING: High CPU usage detected",
       "ERROR: Timeout while calling external API",
       "INFO: User logged out"
   ]
2. Create a generator function called 'filter_error_logs(log_lines: list)'.
3. Inside the function, iterate over 'log_lines' using a for-loop.
4. If the line starts with "ERROR:" (or contains "ERROR"), 'yield' that line.
5. OUTSIDE the function, iterate over 'filter_error_logs(mock_log_file)' using a for-loop and print each yielded error line.
"""

mock_log_file = [
    "INFO: User Isaque logged in",
    "ERROR: Database connection failed",
    "INFO: Page rendered successfully",
    "WARNING: High CPU usage detected",
    "ERROR: Timeout while calling external API",
    "INFO: User logged out"
    ]

def filter_error_logs(log_lines: list):
    for line in log_lines:
        if "ERROR" in line:
            yield line

logs = filter_error_logs(mock_log_file)
for log in logs:
    print(log)
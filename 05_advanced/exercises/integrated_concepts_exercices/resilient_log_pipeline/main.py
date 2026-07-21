"""
Project 1: Resilient Log Pipeline
Folder: 01_resilient_log_pipeline/
Main File: main.py

Rules:
1. Create a dummy log file named 'server_logs.txt' using a Context Manager ("w"). 
   Write 100 lines: most formatted as "INFO:200:Success", some as "ERROR:500:Internal Fault", 
   and intentionally insert 5 corrupted lines like "INVALID_LINE_NO_DELIMITER" or "INFO:INVALID_CODE:Test".

2. The Decorator: Create an '@execution_timer' decorator that measures and prints how long a function takes to run.

3. The Generator (Lazy Reader): Create a generator function 'stream_logs(file_path: str)'.
   - Use a 'with open(file_path, "r")' block inside the generator.
   - Loop through the file line by line and 'yield' each line stripped of whitespace.

4. The Processor (Error Handling): Create a function 'process_pipeline(file_path: str)' decorated with '@execution_timer'.
   - Iterate over 'stream_logs(file_path)'.
   - Use a 'try/except ValueError' block to split each line by the colon (":").
   - Try to convert the middle element (status code) into an integer using 'int(code)'.
   - If a line is corrupted (IndexError or ValueError), catch the exception, print a warning like "[SKIP] Malformed log line: ...", and continue the loop using 'continue'.
   - Collect valid logs into two counts: 'success_count' and 'error_count', then print the final summary.
"""

from resilient_log_pipeline_context_manager import Log
from process_pipeline import process_pipeline

server_logs = Log("server_logs.txt")
server_logs.log_creator()

logs = server_logs.stream_logs()
for i in range(100):
    print(next(logs))

process_pipeline(server_logs.get_filename_path())
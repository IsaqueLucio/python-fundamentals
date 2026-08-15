"""
Python Core - 06 Libraries (requests)
Exercise 10: The Chunked File Downloader (Easy - Fixation)
Folder: 10_chunked_file_downloader/
Main File: main.py

Rules:
1. Import 'requests' and 'os'.
2. We need to download a binary payload without overloading our computer's RAM.
   Define the target URL: url = "https://httpbin.org/bytes/100000" (Generates a 100 KB binary file).
3. Define an output filepath: filepath = "downloaded_data.bin"
4. Open a GET request using a Context Manager ('with requests.get(...) as response:') 
   and pass 'stream=True' and 'timeout=10'.
5. Inside the 'with' block, call 'response.raise_for_status()'.
6. Extract and print the total file size reported by the server using 'response.headers.get("content-length")'.
7. Open the local file in binary write mode ('with open(filepath, "wb") as file:').
8. Loop through the streamed response using 'response.iter_content(chunk_size=8192)' (8 KB chunks).
9. Write each non-empty chunk to the local file.
10. Outside the loop, print a success message showing the actual file size on your disk using 'os.path.getsize(filepath)'.
11. Finally, clean up by deleting the file using 'os.remove(filepath)'.
"""

import requests, os

url = "https://httpbin.org/bytes/100000"

file_path = os.path.join(os.path.dirname(__file__), "downloaded_data.bin")

with requests.get(url, stream= True, timeout=10) as response:
    try:
        response.raise_for_status()
        file_size = response.headers.get("content-length")
        print(f"Total size of the file: {file_size}.")
        with open(file_path,"wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        real_file_size = os.path.getsize(file_path)
        print(f"The real size of the file is: {real_file_size}.")
        #os.remove(file_path)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR]: {e}.")


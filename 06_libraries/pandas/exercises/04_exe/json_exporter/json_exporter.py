"""
Python Core - 06 Libraries (pandas)
Exercise 10: The JSON Exporter (Easy - Fixation)
Folder: 10_json_exporter/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd'.
2. Create a DataFrame representing active server instances:
   data = {
       "ServerID": ["SRV-01", "SRV-02", "SRV-03"],
       "Status": ["Online", "Offline", "Online"],
       "CPU_Usage": [45.5, 0.0, 88.2]
   }
   df = pd.DataFrame(data)
3. Step A (Dictionary Payload):
   - Convert the DataFrame into a list of dictionaries using '.to_dict(orient="records")'.
   - Save it to a variable named 'api_payload'.
4. Step B (Validation):
   - Loop through 'api_payload' and print each dictionary to verify it is ready to be sent as a JSON response.
"""
#1
import pandas as pd
#2
print("")
data = {
    "ServerID": ["SRV-01", "SRV-02", "SRV-03"],
    "Status": ["Online", "Offline", "Online"],
    "CPU_Usage": [45.5, 0.0, 88.2]
}
df = pd.DataFrame(data)
print(f"Original Data: \n{df}")
#3
print("")
api_payload = df.to_dict(orient="records")
#4
print("Data converted to dict: ")
for record in api_payload:
    print(record)
print("Ready to be sent as a JSON response!")

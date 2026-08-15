"""
Python Core - 06 Libraries (pandas)
Exercise 11: The Payload Parser (Intermediate - Logic & Interpretation)
Folder: 11_payload_parser/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd' and 'io'.
2. Here is a raw JSON string simulating an incoming request from a frontend:
   incoming_json = '''
   [
       {"Device": "Sensor_A", "Temp": 22.5, "Active": true},
       {"Device": "Sensor_B", "Temp": null, "Active": false},
       {"Device": "Sensor_C", "Temp": 24.1, "Active": true}
   ]
   '''
3. Step A (Parsing):
   - Use 'io.StringIO(incoming_json)' to wrap the string.
   - Use 'pd.read_json()' to convert this incoming data directly into a Pandas DataFrame.
4. Step B (Filtering):
   - Filter the DataFrame to keep ONLY the devices where "Active" is True.
   - Print this filtered DataFrame.
"""
#1
import pandas as pd
import io
#2
print("")
incoming_json = '''
   [
       {"Device": "Sensor_A", "Temp": 22.5, "Active": true},
       {"Device": "Sensor_B", "Temp": null, "Active": false},
       {"Device": "Sensor_C", "Temp": 24.1, "Active": true}
   ]
   '''
#3
print("")
json_to_df = pd.read_json(io.StringIO(incoming_json))
print(json_to_df)
#4
print("")
final_df = json_to_df[json_to_df["Active"] == True]
print(f"Final DataFrame: \n{final_df}")
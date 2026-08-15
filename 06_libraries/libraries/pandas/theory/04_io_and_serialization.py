"""
Python Core - 06 Libraries
Module: pandas
File: 04_io_and_serialization.py
Description: Reading and writing DataFrames to CSV, JSON, and Python Dictionaries for API integration.
"""
import pandas as pd

print("--- 1. Creating the Base Data ---")
data = {
    "UserID": [1, 2, 3],
    "Username": ["admin", "guest", "tester"],
    "Role": ["SuperAdmin", "User", "QA"],
    "Is_Active": [True, True, False]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n" + "="*60 + "\n")

print("--- 2. The API Secret Weapon: to_dict() ---")
# APIs in Python (like FastAPI) work natively with Python dictionaries before converting them to JSON.
# The 'records' orientation transforms the table into a List of Dictionaries (Row by Row).
# This is exactly how REST APIs expect to send tabular data!
api_payload = df.to_dict(orient="records")

print("Data converted to API Payload (List of Dicts):")
for record in api_payload:
    print(record)
print("\n" + "="*60 + "\n")

print("--- 3. Working with JSON Strings ---")
# If you need raw JSON text (e.g., to save in a text file or cache in Redis):
json_string = df.to_json(orient="records", indent=2)
print("Raw JSON String:")
print(json_string)
print("\n" + "="*60 + "\n")


print("--- 4. Reading External Data (Mocking a File Read) ---")
# In the real world, you will use pd.read_csv("file.csv") or pd.read_json("file.json").
# Let's mock receiving a JSON payload from a frontend application and converting it BACK to a DataFrame:
incoming_json_payload = '[{"UserID": 4, "Username": "new_guy", "Role": "User", "Is_Active": true}]'

# Convert the raw JSON string back into a powerful Pandas DataFrame:
import io
df_incoming = pd.read_json(io.StringIO(incoming_json_payload))

print("DataFrame constructed from incoming JSON:")
print(df_incoming)
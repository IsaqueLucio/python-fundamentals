"""
Python Core - 06 Libraries (pandas)
Exercise 16: The Ultimate Backend Mock (Integrated)
Folder: 16_integrated_backend_mock/
Main File: main.py

Objective: Simulate a complete backend endpoint. Read two JSON payloads, join them, clean data, aggregate, and return a clean JSON payload.

Rules:
1. Import 'pandas' as 'pd' and 'io'.
2. The incoming payloads:
   users_json = '''[
       {"UserID": 1, "Name": "Alice"},
       {"UserID": 2, "Name": "Bob"},
       {"UserID": 3, "Name": "Charlie"}
   ]'''
   
   orders_json = '''[
       {"OrderID": 101, "UserID": 1, "Amount": 250.0},
       {"OrderID": 102, "UserID": 1, "Amount": 50.0},
       {"OrderID": 103, "UserID": 2, "Amount": null}
   ]'''
3. Step A (Ingestion):
   - Parse both JSON strings into separate DataFrames.
4. Step B (Merge & Clean):
   - Perform a LEFT JOIN using users as the main table. (This ensures Charlie stays in the report even with no orders).
   - Fill any NaN values in the 'Amount' column with 0.0.
5. Step C (Aggregate & Export):
   - Group by 'Name' and calculate the sum of 'Amount'.
   - Reset the index.
   - Export the result as a list of dictionaries (orient="records") and print it.
"""
#1
import pandas as pd
import io
#2
users_json = '''[
      {"UserID": 1, "Name": "Alice"},
      {"UserID": 2, "Name": "Bob"},
      {"UserID": 3, "Name": "Charlie"}
   ]''' 
orders_json = '''[
      {"OrderID": 101, "UserID": 1, "Amount": 250.0},
      {"OrderID": 102, "UserID": 1, "Amount": 50.0},
      {"OrderID": 103, "UserID": 2, "Amount": null}
   ]'''
#3
temp_users = pd.read_json(io.StringIO(users_json))
temp_orders = pd.read_json(io.StringIO(orders_json))
users = pd.DataFrame(temp_users)
orders = pd.DataFrame(temp_orders)
#4
merge_df = pd.merge(users, orders,on="UserID",how="left")
merge_df["Amount"] = merge_df["Amount"].fillna(0.0)
#5
final = merge_df.groupby("Name").agg({"Amount": ["sum"]}).reset_index()
api_result = final.to_dict(orient="records")
for line in api_result:
    print(line)
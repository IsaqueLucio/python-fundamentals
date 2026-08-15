"""
Python Core - 06 Libraries (pandas)
Exercise 12: The Full API Cycle (Hard - Problem Solving)
Folder: 12_full_api_cycle/
Main File: main.py

Scenario:
An external API sent a JSON payload containing daily sales, but it has missing values. 
Your backend needs to parse it, clean the missing numerical data, calculate the total revenue per store, and export it back as a clean list of dictionaries ready to be sent to the database.

Rules:
1. Import 'pandas' as 'pd' and 'io'.
2. The incoming corrupted JSON payload:
   raw_payload = '''
   [
       {"Store": "North", "Revenue": 1500.0},
       {"Store": "South", "Revenue": 2000.0},
       {"Store": "North", "Revenue": null},
       {"Store": "East",  "Revenue": 800.0},
       {"Store": "South", "Revenue": 2500.0}
   ]
   '''
3. Step A (Parse and Clean):
   - Convert the 'raw_payload' into a DataFrame using 'pd.read_json()' and 'io.StringIO()'.
   - Fill the missing (NaN) "Revenue" values with 0.0 using '.fillna(0)'.
4. Step B (Aggregate):
   - Group the cleaned DataFrame by "Store".
   - Calculate the sum of the "Revenue" for each store.
   - IMPORTANT: '.groupby().sum()' moves the grouped column into the Index. Use '.reset_index()' right after your aggregation to turn "Store" back into a normal column! 
     Example: df.groupby('Col')['Rev'].sum().reset_index()
5. Step C (Export):
   - Convert the final aggregated DataFrame back into a list of dictionaries (orient="records").
   - Print the final exported payload.
"""
#1
import pandas as pd
import io
#2
raw_payload = '''
   [
      {"Store": "North", "Revenue": 1500.0},
      {"Store": "South", "Revenue": 2000.0},
      {"Store": "North", "Revenue": null},
      {"Store": "East",  "Revenue": 800.0},
      {"Store": "South", "Revenue": 2500.0}
   ]
 '''
#3
df_raw_pay = pd.read_json(io.StringIO(raw_payload))
df_raw_pay["Revenue"] = df_raw_pay["Revenue"].fillna(0.0)
#4
total_rev = df_raw_pay.groupby("Store")["Revenue"].sum().reset_index()
final_dict_payload = total_rev.to_dict(orient="records")
print("Final exported payload:")
for line in final_dict_payload:
    print(line)
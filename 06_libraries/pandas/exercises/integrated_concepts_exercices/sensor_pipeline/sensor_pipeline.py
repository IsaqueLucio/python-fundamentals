"""
Python Core - 06 Libraries (pandas)
Exercise 15: The Sensor Pipeline (Integrated)
Folder: 15_integrated_sensor_pipeline/
Main File: main.py

Objective: Parse incoming JSON text, handle missing values, and extract analytical metrics.

Rules:
1. Import 'pandas' as 'pd' and 'io'.
2. The incoming JSON string:
   json_payload = '''
   [
       {"Location": "Zone_1", "Temp": 22.5, "Humidity": 45},
       {"Location": "Zone_2", "Temp": null, "Humidity": 50},
       {"Location": "Zone_1", "Temp": 23.0, "Humidity": 48},
       {"Location": "Zone_3", "Temp": 19.5, "Humidity": null}
   ]
   '''
3. Step A (Ingestion):
   - Parse the JSON string into a DataFrame.
4. Step B (Cleaning):
   - Fill NaN values in 'Temp' with the average temperature of the entire DataFrame (df['Temp'].mean()).
   - Fill NaN values in 'Humidity' with 0.
5. Step C (Aggregation):
   - Group by 'Location'.
   - Use '.agg()' to get the 'mean' for 'Temp' and 'max' for 'Humidity'.
   - Reset the index.
   - Print the final metrics table.
"""
#1
import pandas as pd
import io
#2
json_payload = '''
   [
       {"Location": "Zone_1", "Temp": 22.5, "Humidity": 45},
       {"Location": "Zone_2", "Temp": null, "Humidity": 50},
       {"Location": "Zone_1", "Temp": 23.0, "Humidity": 48},
       {"Location": "Zone_3", "Temp": 19.5, "Humidity": null}
   ]
   '''
#3
df = pd.read_json(io.StringIO(json_payload))
#4
df["Temp"] = df["Temp"].fillna(df["Temp"].mean())
df["Humidity"] = df["Humidity"].fillna(0)
#5
metrics_table = df.groupby("Location").agg({
    "Temp": ["mean"],
    "Humidity": ["max"]
}).reset_index()
print(metrics_table)
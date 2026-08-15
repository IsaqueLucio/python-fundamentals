"""
Python Core - 06 Libraries
Exercise 17: The API Data Fetcher
Folder: 17_api_data_fetcher/
Main File: main.py

Objective: Fetch JSON from a public API, convert to a DataFrame, and apply a NumPy vectorized condition.

Rules:
1. Import 'requests', 'pandas' as 'pd', and 'numpy' as 'np'.
2. Make a GET request to 'https://jsonplaceholder.typicode.com/users'.
3. Parse the JSON response using '.json()'.
4. Convert the JSON into a Pandas DataFrame.
5. Use 'np.where()' to create a new column called 'ID_Type'. If 'id' is even (id % 2 == 0), the value should be "Even", otherwise "Odd".
6. Print the columns: 'id', 'name', and 'ID_Type'.
"""
#1
import numpy as np
import pandas as pd
import requests
#2
try:
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    #3
    json_file = response.json()
    #4
    df = pd.DataFrame(json_file)
    #5
    df["ID_Type"] = np.where(df['id']%2==0,"Even", "Odd")
    #6
    print(f"ID Column: \n{df['id']}")
    print(f"Name Column: \n{df['name']}")
    print(f"ID_Type Column: \n{df['ID_Type']}")
except requests.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")
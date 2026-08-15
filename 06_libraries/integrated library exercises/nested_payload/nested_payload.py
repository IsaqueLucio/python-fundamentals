"""
Python Core - 06 Libraries
Exercise 19: The Nested Payload
Folder: 19_nested_payload/
Main File: main.py

Objective: Handle deeply nested JSON arrays from an API, flatten them, and apply NumPy statistical functions.

Rules:
1. Import 'requests', 'pandas' as 'pd', and 'numpy' as 'np'.
2. Make a GET request to 'https://randomuser.me/api/?results=50'.
3. Extract the 'results' list from the JSON response dictionary.
4. Use 'pd.json_normalize()' to flatten the nested list into a 2D DataFrame.
5. Extract the 'dob.age' column and convert it to a NumPy array using the '.values' attribute.
6. Use 'np.mean()' and 'np.std()' directly on this array to calculate the average age and standard deviation of the users.
7. Print the calculated statistics.
"""
#1
import pandas as pd
import numpy as np
import requests
#2
try:
    url = 'https://randomuser.me/api/?results=50'
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    #3
    data = response.json()
    #4
    df = pd.json_normalize(data["results"])  
    #5
    array = df['dob.age'].to_numpy()
    #6
    mean = np.mean(array)
    stand_devi = np.std(array)
    #7
    print(f"Average age of the users: {mean:.2f}")
    print(f"Standard deviation age of the users: {stand_devi:.2f}")
except requests.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")
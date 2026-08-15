"""
Python Core - 06 Libraries
Exercise 20: Data Corrupter & Healer
Folder: 20_data_corrupter_healer/
Main File: main.py

Objective: Simulate data loss using NumPy random injection and heal it using Pandas methods.

Rules:
1. Import 'requests', 'pandas' as 'pd', and 'numpy' as 'np'.
2. Make a GET request to 'https://jsonplaceholder.typicode.com/todos'.
3. Load the response into a DataFrame and keep only the first 20 rows using 'df.head(20)'.
4. Convert the 'userId' column to float using '.astype(float)' (this is necessary to hold NaN values).
5. Use 'np.random.seed(42)' for reproducibility. Then, use 'np.random.choice()' to randomly select 5 index numbers from the DataFrame's index.
6. Use Pandas '.loc[]' to inject 'np.nan' into the 'userId' column at those 5 selected indices.
7. Print the DataFrame to show the corrupted data.
8. Heal the DataFrame by filling the NaNs with the median of the 'userId' column using '.fillna()'.
9. Print the completely healed DataFrame.
"""
#1
import pandas as pd
import numpy as np
import requests
#2
try:
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url, timeout=10)
    #3
    json = response.json()
    temp = pd.DataFrame(json)
    df = temp.head(20).copy()
    #4
    df['userId'] = df['userId'].astype(float)
    #5
    np.random.seed(42)
    ri = np.random.choice(df.index, size=5, replace=False)
    #6
    df.loc[ri, 'userId'] = np.nan
    #7
    print(df)
    #8
    df['userId'] = df['userId'].fillna(np.nanmedian(df['userId']))
    #9
    print("")
    print(df)
except requests.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")
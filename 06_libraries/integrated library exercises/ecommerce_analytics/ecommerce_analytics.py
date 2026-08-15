"""
Python Core - 06 Libraries
Exercise 18: E-commerce Mock Analytics
Folder: 18_ecommerce_analytics/
Main File: main.py

Objective: Ingest product data from an API, manipulate prices with NumPy, and aggregate with Pandas.

Rules:
1. Import 'requests', 'pandas' as 'pd', and 'numpy' as 'np'.
2. Make a GET request to 'https://fakestoreapi.com/products'.
3. Convert the response to a DataFrame.
4. Use 'np.ceil()' to round up all values in the 'price' column and store them in a new column 'Price_Rounded'.
5. Group the DataFrame by 'category' and calculate the mean of 'Price_Rounded' for each category.
6. Print the resulting aggregated DataFrame.
"""
#1
import pandas as pd
import numpy as np
import requests
#2
try:
    url =  'https://fakestoreapi.com/products'
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    json = response.json()
    #3
    df = pd.DataFrame(json)
    #4
    df['Price_Rounded'] = np.ceil(df['price'])
    #5
    final = df.groupby("category").agg({"Price_Rounded": ["mean"]})
    #6
    print(final)
except requests.RequestException as e:
    print(f"[ERROR] {e}.")
except Exception as a:
    print(f"[ERROR] {a}.")
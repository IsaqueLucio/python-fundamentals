"""
Python Core - 06 Libraries (pandas)
Exercise 5: The Imputation and Duplication (Intermediate - Logic & Interpretation)
Folder: 05_imputation_and_duplication/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd' and 'numpy' as 'np'.
2. Create a DataFrame representing product prices in a catalog. Notice the duplicate row and the missing prices:
   data = {
       "ProductID": ["P1", "P2", "P3", "P2", "P4"],
       "Category": ["Electronics", "Books", "Clothing", "Books", "Electronics"],
       "Price": [299.99, 15.50, np.nan, 15.50, np.nan]
   }
   df = pd.DataFrame(data)
3. Step A (Deduplication):
   - Find and print the number of duplicate rows using '.duplicated().sum()'.
   - Drop the duplicate rows using '.drop_duplicates()' (keep the first one). Save the result back to 'df'.
4. Step B (Imputation):
   - Calculate the MEDIAN price of the remaining valid products in the "Price" column.
   - Use '.fillna()' to replace the NaNs in the "Price" column with this calculated median.
   - Print the final, deduplicated, and fully imputed DataFrame.
"""
#1
import pandas as pd
import numpy as np
#2
print("")
data = {
   "ProductID":["P1", "P2", "P3", "P2", "P4"],
   "Category": ["Electronics", "Books", "Clothing", "Books", "Electronics"],
   "Price":    [299.99, 15.50, np.nan, 15.50, np.nan]
}
df = pd.DataFrame(data)
print(f"Original DataFrame: \n{df}")
#3
print("")
print(f"Number of duplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates(keep="first")
#4
median_price = df["Price"].median()
print(f"Median prices: ${median_price}")
df["Price"] = df["Price"].fillna(median_price)
print("")
print(f"Final DataFrame: \n{df}")
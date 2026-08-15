"""
Python Core - 06 Libraries (pandas)
Exercise 14: The Inventory Sync (Integrated)
Folder: 14_integrated_inventory_sync/
Main File: main.py

Objective: Combine product catalog with stock status, calculate assets, and export as an API payload.

Rules:
1. Import 'pandas' as 'pd'.
2. The datasets:
   catalog = pd.DataFrame({
       "SKU": ["A1", "A2", "A3"],
       "Product": ["Laptop", "Mouse", "Keyboard"],
       "Price": [1200.0, 25.0, 75.0]
   })
   
   stock = pd.DataFrame({
       "SKU": ["A1", "A2", "A3"],
       "Warehouse": ["NY", "NY", "CA"],
       "Quantity": [10, 150, 40]
   })
3. Step A (Merge):
   - Perform an INNER JOIN between 'catalog' and 'stock' on "SKU".
4. Step B (Derived Column):
   - Create a 'Total_Value' column (Price * Quantity).
5. Step C (Export):
   - Convert the merged DataFrame into a list of dictionaries (orient="records").
   - Iterate and print each dictionary.
"""
#1
import pandas as pd
#2
catalog = pd.DataFrame({
      "SKU": ["A1", "A2", "A3"],
      "Product": ["Laptop", "Mouse", "Keyboard"],
      "Price": [1200.0, 25.0, 75.0]
   })
stock = pd.DataFrame({
      "SKU": ["A1", "A2", "A3"],
      "Warehouse": ["NY", "NY", "CA"],
      "Quantity": [10, 150, 40]
   })
#3
inner_join = pd.merge(catalog, stock, on="SKU", how="inner")
#4
inner_join["Total_Value"] = inner_join["Price"] * inner_join["Quantity"]
#5
final = inner_join.to_dict(orient="records")
for line in final:
    print(line)
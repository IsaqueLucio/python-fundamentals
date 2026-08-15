"""
Python Core - 06 Libraries (pandas)
Exercise 6: The Type Coercion Pipeline (Hard - Problem Solving)
Folder: 06_type_coercion_pipeline/
Main File: main.py

Scenario:
You are building an ETL pipeline. An external API sent you an inventory dataset, but the "Stock_Quantity" column is corrupted. It arrived as text (strings), and some values are completely invalid ("Out of Stock", "N/A"). You must safely convert this column to integers without crashing the application.

Rules:
1. Import 'pandas' as 'pd'.
2. Create the corrupted DataFrame:
   data = {
       "Item": ["Laptop", "Mouse", "Keyboard", "Monitor", "Cables"],
       "Stock_Quantity": ["50", "120", "Out of Stock", "45", "N/A"]
   }
   df = pd.DataFrame(data)
3. Step A (Safe Conversion):
   - Use 'pd.to_numeric()' with the 'errors="coerce"' parameter on the "Stock_Quantity" column. 
   - This will turn the valid numbers into floats and the garbage text ("Out of Stock", "N/A") into NaNs.
4. Step B (Filling and Casting):
   - Now that the garbage is converted to NaNs, fill those NaNs with a default stock value of 0 using '.fillna(0)'.
   - Finally, chain the '.astype(int)' method to convert the whole column into clean integers.
5. Validation:
   - Print the final DataFrame.
   - Print the '.dtypes' of the DataFrame to prove that "Stock_Quantity" is now a true integer (int32 or int64)!
"""
#1
import pandas as pd
#2
print("")
data = {
   "Item": ["Laptop", "Mouse", "Keyboard", "Monitor", "Cables"],
   "Stock_Quantity": ["50", "120", "Out of Stock", "45", "N/A"]
   }
df = pd.DataFrame(data)
print(f"Corrupted DataFrame: \n{df}")
#3
print("")
df["Stock_Quantity"] = pd.to_numeric(df["Stock_Quantity"], errors="coerce")
print(f"Converting the corrupted data into NaNs: \n{df}")
#4
df["Stock_Quantity"] = df["Stock_Quantity"].fillna(0).astype(int)
#5
print("")
print(f"Final DataFrame: \n{df}\n")
print(f"Final DataFrame type data: \n{df.dtypes}")


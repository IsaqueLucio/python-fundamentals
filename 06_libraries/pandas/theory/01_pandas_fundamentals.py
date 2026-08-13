"""
Python Core - 06 Libraries
Module: pandas
File: 01_pandas_fundamentals.py
Description: Mastering Series, DataFrames, indexing (loc/iloc), and basic tabular filtering.
"""
import pandas as pd

print("--- 1. The Core Building Block: Pandas Series ---")
# A Series is a 1D array with an explicit index (like a single column in Excel).
sales = pd.Series([150, 200, 300], index=["Jan", "Feb", "Mar"])
print("Sales Series:")
print(sales)
print(f"\nValue in February: {sales['Feb']}")
print("\n" + "="*60 + "\n")


print("--- 2. The Mighty DataFrame ---")
# A DataFrame is a 2D table. The most common way to create one in code is using a Dictionary.
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "Engineering", "Engineering", "Sales"],
    "Salary": [6500, 9200, 8800, 7100]
}
df = pd.DataFrame(data)
print("Corporate DataFrame:")
print(df)
print("\n" + "="*60 + "\n")


print("--- 3. Navigation: loc vs iloc ---")
# .iloc (Integer Location): Navigates purely by numerical index (just like NumPy arrays).
# Let's get the first row (index 0):
print("First row using .iloc[0]:")
print(df.iloc[0])

# .loc (Label Location): Navigates using the exact names of the rows and columns.
# To make .loc powerful, let's change the index from numbers (0,1,2...) to the Employee names!
df.set_index("Employee", inplace=True)
print("\nDataFrame with 'Employee' as Index:")
print(df)

print("\nCharlie's details using .loc['Charlie']:")
print(df.loc["Charlie"])

print("\nCharlie's Salary specifically: loc['Charlie', 'Salary']")
print(df.loc["Charlie", "Salary"])
print("\n" + "="*60 + "\n")


print("--- 4. Boolean Filtering ---")
# Just like NumPy, we can filter entire tables instantly without writing 'for' loops!
high_earners = df[df["Salary"] > 8000]
print("Employees earning more than $8000:")
print(high_earners)

# Combining conditions requires parentheses and bitwise operators (&, |)
senior_engineers = df[(df["Department"] == "Engineering") & (df["Salary"] > 9000)]
print("\nEngineering team members earning over $9000:")
print(senior_engineers)
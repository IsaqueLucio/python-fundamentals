"""
Python Core - 06 Libraries
Module: pandas
File: 02_data_cleaning_and_nulls.py
Description: Mastering data cleaning, handling missing values (NaN), dropping duplicates, and safe type conversions.
"""
import pandas as pd
import numpy as np

print("--- 1. The Reality of Dirty Data (Missing Values) ---")
# Real databases are full of holes. Pandas represents missing data as NaN (Not a Number) or None.
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Charlie"],
    "Department": ["IT", "Sales", np.nan, "HR", "Sales", "IT", np.nan], # Missing departments
    "Salary": [7500.0, 5200.0, 8100.0, np.nan, 6000.0, 9200.0, 8100.0], # Missing salary
    "Join_Year": ["2020", "2021", "2019", "2022", "2020", "InvalidYear", "2019"] # String numbers and garbage
}

df = pd.DataFrame(data)
print("Raw Dirty DataFrame:")
print(df)


print("\n--- 2. Diagnosing the Mess (.isnull and .info) ---")
# ALWAYS check for nulls before doing any math!
print("Count of missing values per column:")
print(df.isnull().sum())


print("\n--- 3. Handling Missing Data (Imputation vs Dropping) ---")
# Strategy A: Drop rows where CRITICAL data is missing (e.g., Department)
# subset=["Department"] ensures we only drop if the Department is NaN.
df_clean = df.dropna(subset=["Department"]).copy()

# Strategy B: Impute (fill) missing numerical data with a statistical metric (e.g., Median Salary)
median_salary = df_clean["Salary"].median()
# We use .fillna() to replace NaNs safely!
df_clean["Salary"] = df_clean["Salary"].fillna(median_salary)

print("DataFrame after Dropping missing Depts and Filling missing Salaries:")
print(df_clean)


print("\n--- 4. Handling Duplicates ---")
# Charlie was inserted twice by mistake! Let's find and remove duplicates.
print(f"Number of duplicate rows: {df_clean.duplicated().sum()}")

# keep='first' keeps the first occurrence and deletes the rest.
df_clean = df_clean.drop_duplicates(keep="first")


print("\n--- 5. Type Conversion and Handling Corrupted Values (.astype and pd.to_numeric) ---")
# 'Join_Year' is currently a string (object). We need it to be an integer.
# But wait! Frank has "InvalidYear" as a value. A simple .astype(int) will crash the script!

# Solution: pd.to_numeric with errors='coerce' forces invalid data into NaN.
df_clean["Join_Year"] = pd.to_numeric(df_clean["Join_Year"], errors="coerce")

# Now we have a new NaN where "InvalidYear" used to be. Let's fill it with a default year (e.g., 2023)
# and FINALLY convert the whole column to integer!
df_clean["Join_Year"] = df_clean["Join_Year"].fillna(2023).astype(int)

print("\nFinal Pristine DataFrame:")
print(df_clean)
print("\nFinal Data Types:")
print(df_clean.dtypes)
"""
Python Core - 06 Libraries
Module: pandas
File: 03_grouping_and_merging.py
Description: Mastering groupby aggregations, multiple metrics, and SQL-like table merges.
"""
import pandas as pd

print("--- 1. Data Aggregation (Group By) ---")
# A sales record containing multiple transactions from different employees
sales_data = {
    "Employee":   ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "Department": ["HR", "Sales", "HR", "IT", "Sales", "HR"],
    "Revenue":    [200, 500, 300, 400, 600, 150]
}
df_sales = pd.DataFrame(sales_data)

# Goal: What is the total revenue per employee?
# .groupby() groups identical rows, and .sum() sums the numeric values.
revenue_per_employee = df_sales.groupby("Employee")["Revenue"].sum()
print("Total Revenue by Employee:")
print(revenue_per_employee)

# Complex aggregations using .agg() to get multiple metrics at once
department_metrics = df_sales.groupby("Department").agg({
    "Revenue": ["sum", "mean", "count"]
})
print("\nMetrics per Department (Sum, Average, Count):")
print(department_metrics)
print("\n" + "="*60 + "\n")


print("--- 2. Joining Tables (Merge) ---")
# Table 1: User registration information
users_data = {
    "UserID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Location": ["NY", "LA", "SF", "TX"]
}
df_users = pd.DataFrame(users_data)

# Table 2: Transaction history (note that Diana has no transactions and Eve has no registration)
transactions_data = {
    "TransactionID": [101, 102, 103, 104],
    "UserID": [1, 2, 2, 5],
    "Amount": [250.0, 150.0, 300.0, 90.0]
}
df_transactions = pd.DataFrame(transactions_data)

# INNER JOIN (Default): Keeps only the records that exist in BOTH tables.
inner_join = pd.merge(df_users, df_transactions, on="UserID", how="inner")
print("Inner Join (Only matching users and transactions):")
print(inner_join)

# LEFT JOIN: Keeps ALL users from the left table, even without transactions (fills with NaN).
left_join = pd.merge(df_users, df_transactions, on="UserID", how="left")
print("\nLeft Join (All users, NaN for missing transactions):")
print(left_join)
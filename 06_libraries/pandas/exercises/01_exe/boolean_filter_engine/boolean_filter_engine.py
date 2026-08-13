"""
Python Core - 06 Libraries (pandas)
Exercise 3: The Boolean Filter Engine (Hard - Problem Solving)
Folder: 03_boolean_filter_engine/
Main File: main.py

Scenario:
You are analyzing a customer database to launch a targeted marketing campaign. You must extract a highly specific subset of users based on multiple conditions.

Rules:
1. Import 'pandas' as 'pd'.
2. Create the customer DataFrame:
   - "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
   - "Age": [22, 35, 28, 42, 19, 31]
   - "Plan": ["Basic", "Premium", "Premium", "Basic", "Premium", "Premium"]
   - "Monthly_Spend": [15.0, 55.5, 40.0, 20.0, 12.0, 85.0]
3. Step A (Single Condition):
   - Filter the DataFrame to find all customers who have a "Premium" plan.
   - Print this filtered DataFrame.
4. Step B (Multiple Conditions):
   - We only want to target HIGH-VALUE ADULTS.
   - Filter the original DataFrame to find customers who are older than 25 AND spend more than $50.0 monthly.
   - Save this to a variable named 'target_customers' and print it.
5. Step C (Surgical Extraction):
   - The marketing email system only needs the names and spending of the target customers.
   - Using your 'target_customers' subset, extract ONLY the "Name" and "Monthly_Spend" columns.
   - Print this final report.
"""
#1
import pandas as pd
#2
print("")
data = {
   "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
   "Age": [22, 35, 28, 42, 19, 31],
   "Plan": ["Basic", "Premium", "Premium", "Basic", "Premium", "Premium"],
   "Monthly_Spend": [15.0, 55.5, 40.0, 20.0, 12.0, 85.0]
}
customers = pd.DataFrame(data)
print(f"Customers: \n{customers}")
#3
print("")
premium_customers = customers[customers["Plan"] == "Premium"]
print(f"Premium Customers: \n{premium_customers}\n")
#4
print("")
target_customers = customers[(customers["Age"] >= 25) & (customers["Monthly_Spend"] >= 50.0)]
print(f"Target Customers: \n{target_customers}")
#5
print("")
print(f"Name and Monthly Spends of the target customers: \n{target_customers[["Name", "Monthly_Spend"]]}")
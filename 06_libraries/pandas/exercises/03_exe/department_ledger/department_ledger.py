"""
Python Core - 06 Libraries (pandas)
Exercise 7: The Department Ledger (Easy - Fixation)
Folder: 07_department_ledger/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd'.
2. Create the following DataFrame representing company expenses:
   data = {
       "Department":   ["IT", "HR", "IT", "Marketing", "HR", "IT"],
       "Expense_Type": ["Software", "Training", "Hardware", "Ads", "Recruiting", "Cloud"],
       "Cost":         [1200.50, 500.00, 3500.00, 2000.00, 800.00, 450.75]
   }
   df = pd.DataFrame(data)
3. Step A (Basic Grouping):
   - Group the data by "Department".
   - Calculate the total (sum) "Cost" for each department.
   - Print the resulting Series.
4. Step B (Average Metric):
   - Calculate the average (mean) "Cost" for each department.
   - Print this result.
"""
#1
import pandas as pd
#2
print("")
data = {
   "Department":   ["IT", "HR", "IT", "Marketing", "HR", "IT"],
   "Expense_Type": ["Software", "Training", "Hardware", "Ads", "Recruiting", "Cloud"],
   "Cost":         [1200.50, 500.00, 3500.00, 2000.00, 800.00, 450.75]
}
df = pd.DataFrame(data)
print(df)
#3
print("")
data_by_dep = df.groupby("Department")["Cost"].sum()
print(data_by_dep)
#4
print("")
df_metrics = df.groupby("Department").agg({"Cost": ["mean"]})
print(df_metrics)
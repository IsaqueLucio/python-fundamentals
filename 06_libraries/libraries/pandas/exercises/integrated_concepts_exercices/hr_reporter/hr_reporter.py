"""
Python Core - 06 Libraries (pandas)
Exercise 13: The HR Reporter (Integrated)
Folder: 13_integrated_hr_reporter/
Main File: main.py

Objective: Clean dirty data, filter active employees, and generate a payroll report.

Rules:
1. Import 'pandas' as 'pd'.
2. The dirty dataset:
   data = {
       "EmpID": [1, 2, 2, 4, 5],  # Notice the duplicate EmpID 2
       "Name": ["Alice", "Bob", "Bob", "Charlie", "Diana"],
       "Dept": ["IT", "Sales", "Sales", "IT", "HR"],
       "Salary": [7000.0, 5000.0, 5000.0, None, 4500.0],
       "Active": [True, True, True, False, True]
   }
   df = pd.DataFrame(data)
3. Step A (Cleaning):
   - Drop duplicate rows using '.drop_duplicates()'.
   - Fill the missing (NaN) 'Salary' with 0.0.
4. Step B (Filtering):
   - Filter the DataFrame to keep ONLY 'Active' == True.
5. Step C (Aggregation):
   - Group by 'Dept' and calculate the total (sum) 'Salary' for each department.
   - Print the final report.
"""
#1
import pandas as pd
#2
data = {
      "EmpID": [1, 2, 2, 4, 5],
      "Name": ["Alice", "Bob", "Bob", "Charlie", "Diana"],
      "Dept": ["IT", "Sales", "Sales", "IT", "HR"],
      "Salary": [7000.0, 5000.0, 5000.0, None, 4500.0],
      "Active": [True, True, True, False, True]
   }
df = pd.DataFrame(data)
#3
df_temp = df.drop_duplicates(keep="first")
df_temp["Salary"] = df_temp["Salary"].fillna(0.0)
#4
df_clean = df_temp[df_temp["Active"] == True]
#5
final = df_clean.groupby("Dept").agg({"Salary": ["sum"]})
print(f"Final report: \n{final}")
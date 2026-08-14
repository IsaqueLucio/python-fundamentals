"""
Python Core - 06 Libraries (pandas)
Exercise 4: The Missing Data Detective (Easy - Fixation)
Folder: 04_missing_data_detective/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd' and 'numpy' as 'np'.
2. Create a DataFrame representing users registering on a platform:
   data = {
       "UserID": [101, 102, 103, 104, 105],
       "Email": ["alice@email.com", np.nan, "charlie@email.com", "david@email.com", np.nan],
       "Status": ["Active", "Active", "Pending", "Active", "Pending"]
   }
   df = pd.DataFrame(data)
3. Step A (Diagnosis):
   - Print the total count of missing values per column using '.isnull().sum()'.
4. Step B (Dropping):
   - In our system, a user without an email is useless.
   - Use '.dropna()' to permanently remove (using subset=["Email"]) any row where the "Email" is missing.
   - Save it to 'df_clean' and print the final cleaned DataFrame.
"""
#1
import pandas as pd
import numpy as np
#2
print("")
data = {
   "UserID": [101, 102, 103, 104, 105],
   "Email":  ["alice@email.com", np.nan, "charlie@email.com", "david@email.com", np.nan],
   "Status": ["Active", "Active", "Pending", "Active", "Pending"]
}
users_info = pd.DataFrame(data)
print(f"Corrupted User Information: \n{users_info}")
#3
print("")
print("Count of missing values per column:")
print(users_info.isnull().sum())
#4
print("")
clean_users_info = users_info.dropna(subset=["Email"]).copy()
print(f"Users with valid emails: \n{clean_users_info}")
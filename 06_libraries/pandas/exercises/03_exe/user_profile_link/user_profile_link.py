"""
Python Core - 06 Libraries (pandas)
Exercise 8: The User-Profile Link (Intermediate - Logic & Interpretation)
Folder: 08_user_profile_link/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd'.
2. Create two DataFrames:
   users = pd.DataFrame({
       "AccountID": [101, 102, 103, 104],
       "Username": ["admin", "guest_01", "super_user", "tester"]
   })
   
   profiles = pd.DataFrame({
       "AccountID": [101, 103, 105],
       "Bio": ["System admin", "Loves coding", "Data scientist"],
       "Level": [99, 50, 12]
   })
3. Step A (Inner Join):
   - We want to find ONLY the users who have both an account and a completed profile.
   - Merge 'users' and 'profiles' using an INNER join on "AccountID".
   - Print the resulting DataFrame.
4. Step B (Left Join):
   - Now, we want a complete list of ALL registered users, attaching profile data if it exists.
   - Merge 'users' and 'profiles' using a LEFT join on "AccountID".
   - Print this DataFrame (notice how missing profiles become NaN).
"""
#1
import pandas as pd
#2
users = pd.DataFrame({
   "AccountID": [101, 102, 103, 104],
   "Username": ["admin", "guest_01", "super_user", "tester"]
})   
profiles = pd.DataFrame({
   "AccountID": [101, 103, 105],
   "Bio": ["System admin", "Loves coding", "Data scientist"],
   "Level": [99, 50, 12]
})
udf = pd.DataFrame(users)
pdf = pd.DataFrame(profiles)
print(f"Users DataFrame: \n{udf}\n")
print(f"Profiles DataFrame: \n{pdf}")
#3
print("")
inner_join = pd.merge(udf, pdf, on="AccountID", how="inner")
print(f"Merge users and profiles using AccountID (inner): \n{inner_join}")
#4
print("")
left_join = pd.merge(udf, pdf, on="AccountID", how="left")
print(f"Merge users and profiles using AccountID (left): \n{left_join}")

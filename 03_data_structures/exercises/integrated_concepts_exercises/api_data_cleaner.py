"""
Final Challenge 1: API Data Cleaner
File: 13_api_data_cleaner.py

Rules:
1. Create a list of dictionaries called 'raw_users':
   raw_users = [
       {"id": 1, "email": "alice@test.com"},
       {"id": 2, "email": "bob@test.com"},
       {"id": 3, "email": "alice@test.com"}, # Duplicate!
       {"id": 4, "email": "charlie@test.com"}
   ]
2. Create an empty set called 'seen_emails' to track duplicates.
3. Create an empty list called 'clean_users' for the final result.
4. Loop through 'raw_users'. For each user:
   - Check if their email is NOT in 'seen_emails'.
   - If it's not, add the email to 'seen_emails' and append the user dictionary to 'clean_users'.
5. Print the final 'clean_users' list.
"""

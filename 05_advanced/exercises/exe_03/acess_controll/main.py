"""
Exercise 2: Access Control (Authorization Guard)
Main File: main.py

Rules:
1. Create a global dictionary simulating a logged-in user: 
   CURRENT_USER = {"username": "Isaque", "role": "guest"}
2. Create a decorator called 'admin_required(func)'.
3. Inside its wrapper:
   - Check if CURRENT_USER["role"] is equal to "admin".
   - If it IS "admin", execute and return the original function normally.
   - If it is NOT "admin", DO NOT execute the function! Instead, print: 
     f"[SECURITY] Access Denied for user '{CURRENT_USER['username']}'. Admin role required!"
     and return None.
4. Create a function 'delete_database()' that prints "Database deleted successfully!" and returns True.
5. Apply the @admin_required decorator to 'delete_database()'.
6. Test calling 'delete_database()'. (It should be blocked!).
7. Change CURRENT_USER["role"] to "admin" in your code and call 'delete_database()' again. (It should work!).
"""
from admin_required import admin_required
from global_dict import change_role

@admin_required
def delete_database():
    print("Database deleted successfully!")
    return True

delete_database()
change_role("admin")
delete_database()
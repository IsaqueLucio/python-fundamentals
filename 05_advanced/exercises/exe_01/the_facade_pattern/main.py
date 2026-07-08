"""
Exercise 3: The Facade Pattern (Advanced __init__)
Main File: main.py
Dependencies to create: A FOLDER called 'database', and inside it: __init__.py, users.py, orders.py

--- Rules for the 'database' folder ---
1. Create a folder named 'database'.
2. Inside 'database', create 'users.py'.
   - Add a function 'fetch_user(user_id: int) -> str' returning: f"User data for ID {user_id}"
3. Inside 'database', create 'orders.py'.
   - Add a function 'fetch_order(order_id: int) -> str' returning: f"Order data for ID {order_id}"
4. Open the '__init__.py' file. We will use it as a "Facade" (a front desk).
   - Inside '__init__.py', write: 
     from .users import fetch_user
     from .orders import fetch_order
   (The dot '.' means "look in the current package folder").

--- Rules for 'main.py' (This file) ---
1. Because of what you did in __init__.py, you don't need to import 'users' or 'orders' directly!
2. Write this exact import: from database import fetch_user, fetch_order
3. Call both functions passing an ID and print their results.
"""

from database import fetch_order, fetch_user

print(fetch_user(385586))
print(fetch_order(312))
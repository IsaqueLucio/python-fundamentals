"""
Exercise 2: Active Sessions
File: 11_active_sessions.py

Rules:
1. Create an empty set called 'active_users' using: active_users = set()
2. Add the users "Alice", "Bob", and "Charlie" to the set using the .add() method.
3. Charlie logged out. Remove him safely using .discard().
4. Try to safely remove "David" using .discard() (he is not in the set, so it shouldn't crash).
5. Print the final state of the 'active_users' set.
"""

active_users = set()

active_users.add("Alice")
active_users.add("Bob")
active_users.add("Charlie")

print(f"Active users in this moment: \n{active_users}")

active_users.discard("Charlie")
print(f"The user Charlie had logout")

print(f"Active users in this moment: \n{active_users}")

active_users.discard("David")

print(f"Active users in this moment: \n{active_users}")
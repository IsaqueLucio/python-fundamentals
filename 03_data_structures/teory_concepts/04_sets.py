"""
Python Core - 03 Data Structures
File: 04_sets.py
Description: Creating sets, uniqueness, safe removal, and mathematical operations.
"""

print("--- 1. Creation and Uniqueness ---")
# Sets use curly braces {}, just like dictionaries, but without key-value pairs (no colons).
# The most important feature: SETS DO NOT ALLOW DUPLICATES.
emails = {"admin@test.com", "user@test.com", "admin@test.com"}

# "admin@test.com" will only appear once when printed!
print(f"Emails set: {emails}") 

# The ultimate trick: Converting a list to a set is the fastest way to remove duplicates.
raw_ids = [10, 20, 30, 10, 50, 20, 10, 10]
unique_ids = list(set(raw_ids))
print(f"Unique IDs from list: {unique_ids}")


print("\n--- 2. Adding and Removing ---")
# Sets are unordered, so there is no .append() (which implies putting at the end).
# We use .add() instead.
active_users = {"Alice", "Bob"}
active_users.add("Charlie")
active_users.add("Alice") # This is silently ignored because Alice is already there.

# .remove() crashes if the item doesn't exist. 
# .discard() is the backend developer's best friend: it removes if exists, does nothing if it doesn't.
active_users.discard("David") # Safe, no crash.
active_users.remove("Alice")
print(f"Active users after modifications: {active_users}")


print("\n--- 3. Mathematical Operations ---")
# Sets shine when comparing groups of data (just like Venn diagrams in math).
backend_devs = {"Isaque", "Alice", "Bob"}
frontend_devs = {"Alice", "Charlie", "Diana"}

# Intersection: Who is in BOTH sets?
fullstack_devs = backend_devs.intersection(frontend_devs)
print(f"Fullstack devs (in both): {fullstack_devs}")

# Union: Combine both sets (duplicates like Alice are naturally merged into one)
all_devs = backend_devs.union(frontend_devs)
print(f"All developers: {all_devs}")

# Difference: Who is in backend but NOT in frontend?
pure_backend = backend_devs.difference(frontend_devs)
print(f"Pure backend devs: {pure_backend}")
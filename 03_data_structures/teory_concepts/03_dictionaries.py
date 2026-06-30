"""
Python Core - 03 Data Structures
File: 03_dictionaries.py
Description: Creating, accessing, modifying, and iterating over dictionaries.
"""

print("--- 1. Creation and Access ---")
# Dictionaries use curly braces {}.
# Each item is a pair of "key": value, separated by commas.
user = {
    "id": 101,
    "name": "Isaque",
    "role": "Backend Developer",
    "is_active": True
}

# Direct Access using the key in brackets
print(f"User Name: {user['name']}")

# Safe Access using .get()
# If you try user["age"], Python crashes with a KeyError because the key doesn't exist.
# .get() safely returns None (or a default value) instead of crashing.
print(f"User Age (Safe Access): {user.get('age')}") 
print(f"User Age (With Default): {user.get('age', 'Age not provided')}")


print("\n--- 2. Adding and Modifying ---")
# If the key already exists, it updates the value.
user["role"] = "Senior Developer" 

# If the key doesn't exist, it creates a new one automatically.
user["company"] = "Tech Corp" 

print(f"Updated User: {user}")


print("\n--- 3. Removing Items ---")
# .pop(key) removes the key-value pair and returns the value.
# We always use it with a default value (like "Not Found") to avoid errors.
removed_company = user.pop("company", "Not Found")
print(f"Removed company: {removed_company}")

# 'del' also works, but it's riskier because it crashes if the key doesn't exist.
del user["is_active"]
print(f"User after deletions: {user}")


print("\n--- 4. Iterating over Dictionaries ---")
# When you loop a dictionary directly, you only get the keys.
# To get both, we use the .items() method.
print("Iterating with .items():")
for key, value in user.items():
    print(f" - {key.capitalize()}: {value}")

# You can also get only the keys or only the values as lists
print(f"\nJust the keys: {list(user.keys())}")
print(f"Just the values: {list(user.values())}")
"""
Exercise 1: Profile Manager
File: 07_profile_manager.py

Rules:
1. Create a dictionary called 'user_profile' with the following keys and values: 
"name" (your name), "age" (your age), and "role" ("Junior Developer").
2. The user's location is missing. Use .get() to print their "location", 
but provide "Location Unknown" as the default fallback so it doesn't crash.
3. The user got a promotion! Update their "role" key to the value "Senior Developer".
4. Add a completely new key-value pair to the dictionary: "remote" with the boolean value True.
5. Print the final 'user_profile' dictionary to verify the changes.
"""

user_profile = {
    "name": "Jhon",
    "age": 27,
    "role": "Tech Lead"
}
print(user_profile)
print(f"Trying to access the non-existent key 'location' using get: {user_profile.get('location', 'Location Unknown')}")
user_profile |= {'remote': True}
user_profile.setdefault('location','null')
print(user_profile)
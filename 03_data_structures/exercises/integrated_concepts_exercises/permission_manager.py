"""
Final Challenge 2: Permission Manager
File: 14_permission_manager.py

Rules:
1. Create a dictionary called 'system_roles' where values are Tuples:
   system_roles = {
       "admin": ("read", "write", "delete", "invite"),
       "editor": ("read", "write", "publish"),
       "viewer": ("read",)
   }
2. Convert the admin's tuple into a set and the editor's tuple into a set.
3. Use Set operations to find the COMMON permissions between 'admin' and 'editor' (intersection). Print it.
4. Use Set operations to find permissions that the 'admin' has but the 'editor' DOES NOT have (difference). Print it.
"""

system_roles = {
       "admin": ("read", "write", "delete", "invite"),
       "editor": ("read", "write", "publish"),
       "viewer": ("read",)
   }

admin = set(system_roles["admin"])
editor = set(system_roles["editor"])
common_ad_ed = admin.intersection(editor)
ad_ed = admin.difference(editor)

print(f"The common permissions between 'admin' and 'editor' are {common_ad_ed}.")
print(f"Permissions that the 'admin' has but the 'editor' DOES NOT have are {ad_ed}")
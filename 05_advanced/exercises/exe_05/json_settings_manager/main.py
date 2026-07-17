"""
Exercise 2: JSON Settings Manager
Main File: main.py

Rules:
1. Import 'os' and 'json'.
2. Define the secure JSON path:
   json_path = os.path.join(os.path.dirname(__file__), "settings.json")
3. Create a default dictionary:
   default_settings = {
       "theme": "dark",
       "notifications": True,
       "volume": 80
   }
4. Write a 'with open()' block in write mode ("w") and use 'json.dump(default_settings, file, indent=4)' to save it.
5. In a new step, write a 'with open()' block in read mode ("r") and use 'json.load(file)' to load the data into a variable called 'current_settings'.
6. Modify the loaded dictionary in memory:
   - Change "theme" to "light"
   - Change "volume" to 100
7. Open the same file again in write mode ("w") and use 'json.dump(current_settings, file, indent=4)' to save the updated settings back to the disk.
8. Check the subfolder to see the created 'settings.json' file and its updated values!
"""

import os
import json

default_settings = {
   "theme": "dark",
   "notifications": True,
   "volume": 80
}

json_path = os.path.join(os.path.dirname(__file__), "settings.json")

with open(json_path, "w") as json_file:
   json.dump(default_settings, json_file, indent=4)

with open(json_path, "r") as json_file:
   current_settings = json.load(json_file)

current_settings["theme"] = "light"
current_settings["volume"] = 100

with open(json_path, "w") as json_file:
   json.dump(current_settings, json_file, indent=4)


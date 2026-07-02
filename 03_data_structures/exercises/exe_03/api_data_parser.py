"""
Exercise 3: API Data Parser
File: 09_api_data_parser.py

Rules:
1. Imagine you received this dictionary from a weather API:
   weather_data = {"city": "Lisbon", "temperature": 22.5, "humidity": 60, "condition": "Sunny"}
2. You need to display this cleanly to the user. Use a 'for' loop combined with the .items() method to iterate over the dictionary.
3. Inside the loop, print each key and value formatted like this: "- [Key Capitalized]: [Value]".
   (Hint: use key.capitalize() to make the first letter uppercase).
4. After the loop, extract ONLY the keys into a list using .keys() and print that list.
"""

weather_data = {"city": "Lisbon", "temperature": 22.5, "humidity": 60, "condition": "Sunny"}

for key, value in weather_data.items():
    print(f"- {key.capitalize()}: {value}")

weather_data_keys = list(weather_data.keys())
print(weather_data_keys)
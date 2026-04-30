"""
Exercise 3.2: Database Filter
File: 08_data_filter.py

Rules:
1. Create a list of numbers representing user IDs: ids = [12, 55, 50, 102, 34, 8, 99, 150].
2. Use the 'filter()' function combined with a lambda to create a new list containing ONLY IDs greater than 50.
3. Remember to convert the filter result back to a list using list().
4. Print the original list and the filtered list.
"""

user_ids = [12, 55, 50, 102, 34, 8, 99, 150]
ids_greater_than_50 = list(filter(lambda x: x>50, user_ids))
print(f"List of IDs greater than 50: {ids_greater_than_50}")
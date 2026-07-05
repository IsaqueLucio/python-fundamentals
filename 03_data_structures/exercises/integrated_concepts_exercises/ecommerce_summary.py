"""
Final Challenge 3: E-commerce Summary
File: 15_ecommerce_summary.py

Rules:
1. Create a list of Tuples called 'orders'. Each tuple contains (order_id, client_name, items_list):
   orders = [
       (101, "Alice", ["Laptop", "Mouse"]),
       (102, "Bob", ["Keyboard"]),
       (103, "Alice", ["Monitor", "Cable"]),
       (104, "Charlie", ["Desk"])
   ]
2. Create an empty dictionary called 'client_totals'.
3. Loop through the 'orders' list. Use Tuple Unpacking in the loop to get id, name, and items.
4. For each order, count the number of items using len(items).
5. If the client's name is already in 'client_totals', ADD the count to their existing total.
6. If the client is not in the dictionary yet, create a new key with that count.
7. Print the final 'client_totals' dictionary (Expected: Alice should have 4 items).
"""

orders = [
       (101, "Alice", ["Laptop", "Mouse"]),
       (102, "Bob", ["Keyboard"]),
       (103, "Alice", ["Monitor", "Cable"]),
       (104, "Charlie", ["Desk"])
   ]

client_totals = {}

for order_id, client_name, items_list in orders:

    total_items = len(items_list)
    
    if client_name not in client_totals:
        client_totals[client_name] = total_items
    else:
         client_totals[client_name] += total_items

print(client_totals)

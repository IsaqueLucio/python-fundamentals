"""
Exercise 3.3: Inventory Sorter
File: 09_inventory_sorter.py

Rules:
1. Create a list of dictionaries representing products in stock:
   inventory = [
       {"product": "Laptop", "stock": 5},
       {"product": "Mouse", "stock": 42},
       {"product": "Keyboard", "stock": 15}
   ]
2. Use the .sort() method with a 'key' parameter receiving a lambda function.
3. The lambda should extract the "stock" value from each dictionary.
4. Print the sorted inventory. (It should be ordered from lowest to highest stock).
"""

inventory = [
       {"product": "Laptop", "stock": 5},
       {"product": "Mouse", "stock": 42},
       {"product": "Keyboard", "stock": 15}
   ]

inventory.sort(key=lambda product: product["stock"])

for product in inventory:
    print(f"- {product['product']} ({product['stock']})")
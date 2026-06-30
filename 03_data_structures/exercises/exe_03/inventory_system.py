"""
Exercise 2: Inventory System
File: 08_inventory_system.py

Rules:
1. Create a dictionary called 'inventory' with the items: {"laptops": 10, "mice": 50, "keyboards": 25}.
2. A shipment of 5 new laptops arrived. Update the "laptops" key by adding 5 to its current value.
3. A client bought all the keyboards. Use .pop() to remove "keyboards" from the dictionary and save the returned value to a variable called 'sold_items'.
4. Try to remove "monitors" using .pop(). Since it doesn't exist, provide a default value of 0 to prevent a crash, and save it to a variable called 'failed_sale'.
5. Print the summary: "Keyboards sold: [sold_items] | Monitors sold: [failed_sale]".
6. Print the final state of the 'inventory' dictionary.
"""


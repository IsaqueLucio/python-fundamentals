"""
Exercise 1: Unique Visitors
File: 10_unique_visitors.py

Rules:
1. Create a list called 'visitors' with some duplicate IP addresses (strings).
   Example: ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5"]
2. Convert the list to a set to automatically remove the duplicates, and save it in a variable called 'unique_visitors'.
3. Print the original list and the new set to see the difference.
4. Print the total number of unique visitors using the len() function on the set.
"""

visitors = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5"]
unique_visitors = list(set(visitors))

print(f"Original list of IP visitors: \n{visitors}\n")
print(f"List of the IP visitors after the set convertion: \n{unique_visitors}\n")
print(f"The total of IP visitors is: {len(unique_visitors)}")

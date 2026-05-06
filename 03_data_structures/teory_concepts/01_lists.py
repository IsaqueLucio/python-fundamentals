"""
Python Core - 03 Data Structures
File: 01_lists.py
Description: Creating, accessing, modifying, and slicing lists.
"""

print("--- 1. Creation and Access ---")
# Lists are defined by square brackets []
frameworks = ["Django", "Flask", "FastAPI", "Tornado"]

# Normal access (Zero-indexed, like in most programming languages)
print(f"First framework: {frameworks[0]}")

# Python's Superpower: Negative Indices
# -1 always gets the LAST element of the list, -2 gets the second to last, etc.
# This saves you from having to write things like frameworks[len(frameworks)-1]
print(f"Last framework: {frameworks[-1]}")


print("\n--- 2. Adding Items ---")
# .append() places the item at the end of the list (Most common operation)
frameworks.append("Pyramid")
print(f"After append: {frameworks}")

# .insert() places the item at a specific index, pushing the rest forward
frameworks.insert(1, "Bottle") 
print(f"After insert at index 1: {frameworks}")


print("\n--- 3. Removing Items ---")
# .pop() removes and RETURNS the last item of the list (useful for queues/stacks)
removed = frameworks.pop()
print(f"Item removed with pop(): {removed}")

# .pop(index) removes a specific index
frameworks.pop(0) # Removes "Django"
print(f"After pop(0): {frameworks}")

# .remove(value) searches for the exact text/number and removes its first occurrence
frameworks.remove("Flask")
print(f"After remove('Flask'): {frameworks}")


print("\n--- 4. Slicing ---")
# Slicing allows you to grab "chunks" of the list using the [start : end] syntax
# The 'start' index is included, the 'end' index is excluded.
numbers = [0, 10, 20, 30, 40, 50, 60]

print(f"Original list: {numbers}")
print(f"From index 2 to 4: {numbers[2:5]}")       # Grabs 20, 30, 40
print(f"From start up to index 3: {numbers[:4]}") # Grabs 0, 10, 20, 30
print(f"From index 4 to the end: {numbers[4:]}")  # Grabs 40, 50, 60
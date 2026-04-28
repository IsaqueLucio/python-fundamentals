'''
Use a for loop with range() to print the multiplication table of 7 (from 1 to 10).
The output should be "7 x 1 = 7", "7 x 2 = 14", etc.
'''

# 1. Define the number for which we want to print the multiplication table
num = 7

# 2. Use a for loop with range() to iterate from 1 to 10
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
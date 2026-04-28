'''
Create a variable speed. Use the ternary operator 
(the one-line conditional) to create a variable status that 
receives "Fined" if the speed is greater than 80, or "Within the limit" otherwise. Print the status.
'''

# 1. Creating the variables
speed = 100
# 2. Using the ternary operator to determine the status
status = "Fined" if speed > 80 else "Within the limit"
# 3. Printing the result
print(f"Your speed was {speed}. {status}")
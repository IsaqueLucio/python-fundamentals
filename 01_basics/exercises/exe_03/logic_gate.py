'''
Define has_ticket = True and age = 16. Use a structure with pure logical operators (and, or, not)
to create a variable can_enter that is true only if the person has a ticket AND is 18 years old or older.
Print the boolean result.
'''

# 1. Creating the variables
has_ticket = True
age = 16

# 2. Defining the condition for entering
can_enter = has_ticket and age >= 18
print(f"has_ticket and age >= 18: {can_enter}")

'''
Create a variable called given and assign it the value 100. Print the value and the type. On the next line,
reassign the same variable with the text "One Hundred" and print the value and the type again to prove dynamic typing.
'''

# 1. Creating the variable
given = 100
print(f"Variabe 'given' as number: ",given," - The type of the variable is: ",type(given))
# 2. Changing the type of the variable
given = "One Hundred"
print(f"Variabe 'given' as string: ",given," - The type of the variable is: ",type(given))

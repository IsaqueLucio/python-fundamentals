'''
Create a variable correct_password = "python123".
Use a while loop that continues to ask for the password via input()
until the entered word is exactly equal to the correct password.
When the user gets it right, print "Access Granted".
'''

# 1. Define the correct password
correct_password = "python123"

# 2. Initialize a variable to store the user's input
password = 0

# 3. Use a while loop to keep asking for the password until it matches the correct password
while password != correct_password:
   password = input("Input the correct password: ")

print(f"Access Granted")
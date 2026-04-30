"""
Exercise 3.1: Inline Password Verifier
File: 07_inline_verifier.py

Rules:
1. Create a lambda function named 'is_strong_password' that takes one argument 'password'.
2. The lambda should return True if the length of the password is 8 characters or more, and False otherwise.
   Hint: use len(password) >= 8.
3. Test the lambda with a weak password (e.g., "1234") and a strong one (e.g., "my_secure_pass") and print both results.
"""

is_strong_password = lambda password : True if len(password) >= 8 else False

wrong_password = is_strong_password("test")
right_passwrd = is_strong_password("test1234")
print(f"{wrong_password} | {right_passwrd}")

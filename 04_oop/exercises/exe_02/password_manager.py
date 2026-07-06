"""
Exercise 2: Secure Password Manager
File: 07_password_manager.py

Rules:
1. Create a class called 'UserAccount'.
2. The __init__ method takes 'username' (public) and 'initial_password' (private).
3. Create a getter method called 'get_password(self)' that DOES NOT return the real password. It should return a masked string like "********".
4. Create a method called 'change_password(self, old_pass, new_pass)'.
   - Add validation: If 'old_pass' matches the current '__password', update the password to 'new_pass' and print "Password updated successfully".
   - If 'old_pass' is wrong, print "Access Denied: Wrong old password".
5. Create a UserAccount object.
6. Call the getter to print the masked password.
7. Attempt to change the password using the WRONG old password.
8. Attempt to change the password using the CORRECT old password.
"""

class UserAccount:

    def __init__(self, username: str):
        self.username = username
        self.__password = ""

    def get_password(self)-> str:
        return "***********"

    def set_password(self, initial_password: str):
        if self.__password == "":
            self.__password = initial_password
            print("Success, password set successfully.")
        else:
            print("You already have a password set; if you want to update it, use the `change_password` method.")
    
    def change_password(self, old_pass: str, new_pass: str):
        if self.__password == "":
            print("First, set a password.")
            return
        if old_pass == self.__password:
            self.__password = new_pass
            print("Password updated successfully.")
        else:
            print("ERROR: Access Denied: Wrong old password.")

userAccount = UserAccount("Bruce")
print(userAccount.get_password())
userAccount.change_password("Test", "Test2")
userAccount.set_password("password123@")
userAccount.set_password("password123@")
userAccount.change_password("Test3", "Test4")
userAccount.change_password("password123@","new_password123@")

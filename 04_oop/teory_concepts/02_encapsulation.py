"""
Python Core - 04 Object-Oriented Programming
File: 05_encapsulation.py
Description: Public vs Private attributes and using getters/setters.
"""

print("--- 1. Creating the Encapsulated Class ---")

class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        # Public attribute: Can be accessed from anywhere
        self.owner = owner 
        
        # Private attribute (__): Cannot be accessed directly from outside
        self.__balance = initial_balance 

    # Getter Method: A safe way to READ the private data
    def get_balance(self) -> float:
        return self.__balance

    # Setter Method: A safe way to MODIFY the private data (with validation!)
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Error: Insufficient funds or invalid amount.")


print("\n--- 2. Interacting with the Object ---")
account = BankAccount("Alice", 1000.0)

# Accessing the public attribute works fine
print(f"Account Owner: {account.owner}")

# Using the proper 'gates' (methods) to interact with the balance
account.deposit(500)
account.withdraw(200)

# Safely reading the balance using the Getter
print(f"Current Balance check: ${account.get_balance()}")


print("\n--- 3. Attempting to break the rules ---")
# If we try to access or change the private variable directly, it will fail/be ignored.
try:
    print(account.__balance)
except AttributeError:
    print("Security Alert: Cannot access '__balance' directly!")

# What happens if we try to force a change?
account.__balance = 999999  # This actually creates a NEW public variable called __balance
print(f"Fake forced balance: {account.__balance}")
print(f"REAL protected balance: ${account.get_balance()}") # The real money is safe!
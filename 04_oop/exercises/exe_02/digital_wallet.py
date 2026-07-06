"""
Exercise 3: Digital Wallet
File: 08_digital_wallet.py

Rules:
1. Create a class called 'DigitalWallet'.
2. The __init__ method takes 'account_holder' (public). Set a private attribute '__balance' to 0.0.
3. Create a getter method called 'get_balance(self)' that returns the '__balance'.
4. Create a method 'deposit(self, amount)'. If amount is greater than 0, add it to '__balance' and print the new balance.
5. Create a method 'process_payment(self, amount)'. 
   - Add validation: If the amount is greater than 0 AND there is enough balance, subtract it from '__balance' and print a success message.
   - Else, print "Payment failed: Insufficient funds or invalid amount".
6. Create a DigitalWallet object.
7. Deposit 100.
8. Try to process a payment of 150 (should fail).
9. Process a payment of 40 (should succeed).
10. Print the final balance using the getter method.
"""

class DigitalWallet:

    def __init__(self, account_holder: str):
        self.account_holder = account_holder
        self.__balance = 0.0

    def get_balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else: 
            print("Error: Deposit amount must be positive.")

    def process_payment(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount paid ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Error: Insufficient funds or invalid amount.")

obj1 = DigitalWallet("Robert")
obj1.deposit(100)
obj1.process_payment(150)
obj1.process_payment(40)
print(f"Current balance: ${obj1.get_balance()}.")

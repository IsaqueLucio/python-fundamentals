"""
Exercise 3: Payment Methods
File: 18_payment_methods.py

Rules:
1. Import ABC and abstractmethod.
2. Create an abstract class 'PaymentMethod(ABC)' with an abstract method 'pay(self, amount: float)'.
3. Create a child class 'CreditCard' that overrides 'pay' to print: "Paid $[amount] using Credit Card."
4. Create a child class 'PayPal' that overrides 'pay' to print: "Paid $[amount] using PayPal."
5. Create a child class 'BankTransfer' that overrides 'pay' to print: "Paid $[amount] via Bank Transfer."
6. Create a function 'checkout(payment_method, total_amount)'.
   - Inside it, call the 'pay' method on the 'payment_method' object passing the 'total_amount'.
7. Create an instance of CreditCard and call checkout() with it and an amount of 50.0.
8. Create an instance of PayPal and call checkout() with it and an amount of 120.0.
"""

from abc import ABC, abstractmethod
from typing import override

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCard(PaymentMethod):

    @override
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."
    
class PayPal(PaymentMethod):

    @override
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."
    
class BankTransfer(PaymentMethod):

    @override
    def pay(self, amount):
        return f"Paid ${amount} via Bank Transfer."
    
def checkout(payment_method, total_amount):
    print(payment_method.pay(total_amount))

credit_card = CreditCard()
pay_pal = PayPal()
bank_transfer = BankTransfer()

checkout(credit_card, 50.0)
checkout(pay_pal, 120.0)
checkout(bank_transfer, 290.0)
"""
Python Core - 04 Object-Oriented Programming
File: 13_abstract_classes.py
Description: Abstract Base Classes (ABC) and enforcing contracts (Interfaces).
"""

# We need to import the ABC module and the abstractmethod decorator
from abc import ABC, abstractmethod

print("--- 1. Defining the Contract (Interface/Abstract Class) ---")

# By inheriting from ABC, we prevent this class from being instantiated directly.
class PaymentGateway(ABC):
    
    # The @abstractmethod decorator creates a strict rule: 
    # ANY child class MUST create its own version of this method.
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        # We just use 'pass' because the Parent doesn't do the work, it just sets the rule.
        pass

    @abstractmethod
    def refund(self, amount: float) -> str:
        pass


print("\n--- 2. Implementing the Concrete Classes ---")

class StripeProcessor(PaymentGateway):
    # If we forget to write the 'refund' method here, Python will crash when we try to create a StripeProcessor!
    
    def process_payment(self, amount: float) -> str:
        return f"Stripe: Successfully charged ${amount} to credit card."
        
    def refund(self, amount: float) -> str:
        return f"Stripe: Refunded ${amount} to user's bank account."

class CryptoProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f"Crypto: Transferred ${amount} worth of Bitcoin."
        
    def refund(self, amount: float) -> str:
        return f"Crypto: Reversed transaction of ${amount} to origin wallet."


print("\n--- 3. Testing the Enforcement ---")

# UNCOMMENT THE LINE BELOW TO SEE THE ERROR:
# generic_gateway = PaymentGateway() 
# TypeError: Can't instantiate abstract class PaymentGateway...

stripe = StripeProcessor()
crypto = CryptoProcessor()

print(stripe.process_payment(150.0))
print(crypto.refund(50.0))
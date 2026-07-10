"""
Integrated OOP 3: E-commerce Checkout
Main File: main.py
Dependencies to create: payment.py, cart.py

--- Rules for 'payment.py' ---
1. Import ABC and abstractmethod.
2. Create abstract class 'PaymentMethod(ABC)' with abstract method 'process_payment(self, amount: float) -> bool'.
3. Create 'CreditCard(PaymentMethod)'. Override 'process_payment' to print "Charging $[amount] to Credit Card..." and return True.
4. Create 'Pix(PaymentMethod)'. Override 'process_payment' to print "Generating Pix QR Code for $[amount]..." and return True.

--- Rules for 'cart.py' ---
1. Import 'PaymentMethod'.
2. Create 'ShoppingCart'. __init__ initializes an empty list 'items' (each item is just a dictionary like {"name": "Laptop", "price": 1000}) and 'total' = 0.0.
3. Create 'add_item(self, name: str, price: float)'. Append to items and add to total.
4. Create 'checkout(self, payment_method: PaymentMethod)'. 
   - This method receives any payment method (Polymorphism).
   - It calls 'process_payment(self.total)' on the received method.
   - If successful (returns True), print "Checkout complete!" and clear the cart.

--- Rules for 'main.py' (This file) ---
1. Import ShoppingCart, CreditCard, and Pix.
2. Create a cart and add 2 items.
3. Create a CreditCard object.
4. Pass the CreditCard to the cart's checkout method.
"""

from cart import ShoppingCart
from payment import CreditCard, Pix

pix = Pix()
credit_card = CreditCard()
my_cart = ShoppingCart()

print(my_cart.get_cart())
print(my_cart.get_history())

my_cart.add_item("Coat", 99.90)
my_cart.add_item("Sneakers Bar", 5.50)

print(my_cart.get_cart())
print(my_cart.checkout(pix))
print(my_cart.get_history())
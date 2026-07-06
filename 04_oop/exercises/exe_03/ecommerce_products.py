"""
Exercise 2: E-commerce Products
File: 11_ecommerce_products.py

Rules:
1. Create a parent class 'Product' with an __init__ taking 'name' (str) and 'price' (float).
2. Create a method 'get_details(self)' in Product that returns: "[name] costs $[price]."
3. Create a child class 'Electronic' that inherits from Product.
4. The Electronic __init__ must take 'name', 'price', AND 'warranty_months'.
   - Use super().__init__(name, price) to let the parent handle the common data.
   - Save 'warranty_months' as a specific attribute of the Electronic class.
5. Override 'get_details(self)' in Electronic to return: "[name] costs $[price] (Warranty: [warranty_months] months)."
6. Create a child class 'Clothing' inheriting from Product.
7. The Clothing __init__ takes 'name', 'price', and 'size' (str). Use super() appropriately.
8. Override 'get_details(self)' in Clothing to return: "[name] costs $[price] (Size: [size])."
9. Create one Electronic and one Clothing object, and print their details.
"""
from typing import override

class Product:
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
   
    def get_details(self) -> str:
      return f"{self.name} costs ${self.price}."
    
class Eletronic(Product):

   def __init__(self, name, price, warranty_months: int):
      super().__init__(name, price)
      self.warranty_months = warranty_months
   
   @override
   def get_details(self) -> str:
      return f"{self.name} costs ${self.price} (Warranty: {self.warranty_months} months)."

class Clothing(Product):

   def __init__(self, name, price, size: str):
      super().__init__(name, price)
      self.size = size
   
   @override
   def get_details(self) -> str:
      return f"{self.name} costs ${self.price} (Size: {self.size})."

obj1 = Eletronic("Smarphone", 499.90, 12)
obj2 = Clothing("T-shirt", 20.0, "M")
print(obj1.get_details())
print(obj2.get_details())
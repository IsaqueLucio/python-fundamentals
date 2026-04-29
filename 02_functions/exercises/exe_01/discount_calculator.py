"""
Exercise 1.1: Discount Calculator
File: 01_discount_calculator.py

Rules:
1. Create a function called 'calculate_discount' that takes two parameters: 'price' and 'discount_percentage'.
2. The 'discount_percentage' should have a default value of 10.
3. Inside the function, calculate the new price and print: "Original: R$[price] | With discount: R$[new_price]".
4. Call the function once passing only the price (e.g., 100).
5. Call the function again passing both the price (e.g., 200) and a custom discount (e.g., 20).
"""

# 1. Creating the function called 'calculate_discount' that takes two parameters: 'price' and 'discount_percentage'.
def calculate_discount(price, discount_percentage = 10): # 2. The 'discount_percentage' should have a default value of 10.
    # 3. Inside the function, calculate the new price
    new_price = price-((price/100)*discount_percentage)
    # print: "Original: R$[price] | With discount: R$[new_price]"
    print(f"Original: R$ {price} |  With discount of {discount_percentage}%: R$ {new_price}")
# 4. Call the function once passing only the price (e.g., 100).
calculate_discount(100)
# 5. Call the function again passing both the price (e.g., 200) and a custom discount (e.g., 20).
calculate_discount(200, 20)

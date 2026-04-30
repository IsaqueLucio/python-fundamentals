"""
Challenge 1: E-commerce Cart Calculator
File: 10_cart_calculator.py

Rules:
1. Create a function called 'calculate_total'.
2. Use Type Hinting. It should return a 'float'.
3. The first parameter must be 'discount_rate' (float) with a default value of 0.0.
4. The second parameter must be '*prices' to accept any number of item prices.
5. Inside the function, sum all the prices.
6. Apply the discount (e.g., a discount_rate of 0.10 means 10% off the total).
7. Return the final calculated total.
8. Test 1: Call the function with ONLY prices (e.g., 50.0, 100.0, 50.0). The total should be 200.0.
9. Test 2: Call the function passing a 0.20 discount first, followed by the same prices. The total should be 160.0.
"""

def calculate_total(discount_rate = 0.0, *prices: float) -> float:
    prices_sum = sum(prices)
    result = prices_sum - (prices_sum*discount_rate)
    return result

test_1 = calculate_total(0.0,50.0, 100.0, 50.0)
test_2 = calculate_total(0.20, 50.0, 100.0, 50.0)
print(f"Result of test 1: {test_1}\nResult of test 2: {test_2}")
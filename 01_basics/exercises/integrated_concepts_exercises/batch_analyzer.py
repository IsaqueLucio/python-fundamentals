"""
Challenge 3: Batch Analyzer
File: 13_batch_analyzer.py

Rules:
1. Ask the user: "How many products do you want to register?" (convert to int).
2. Use a 'for' loop with 'range()' based on the number entered above.
3. Inside the loop, ask for the "Product weight" (float).
4. If the weight is negative, print "Invalid weight" and use 'continue' to skip to the next iteration.
5. If the weight is greater than 10.0, count it as a "Heavy Product".
6. At the end of the program, print the total number of valid heavy products registered.
"""

# 1. Asking the user how many products him wants to register
num_products = int(input("How many products do you want to register?\n"))
num_of_valid_heavy_products = 0

# 2. Using a 'for' loop with 'range()' based on the number entered above
for i in range(num_products):
    # 3. Asking for the product weight
    product_weight = float(input(f"What is the weight of the {i+1}° product? "))
    # 4. If the weight is negative, print "Invalid weight" and use 'continue' to skip to the next iteration
    if product_weight < 0:
        print("Invalid weight!")
        continue
    # 5. If the weight is greater than 10.0
    elif product_weight > 10:
        # count it as a "Heavy Product"
        num_of_valid_heavy_products += 1

# 6. At the end of the program, print the total number of valid heavy products registered.
print(f"The total of valid heavy products registered is {num_of_valid_heavy_products}.")
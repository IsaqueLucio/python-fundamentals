"""
Challenge: Smart Delivery System

Create a function (or class) that receives the purchase value, the
distance in km, and the customer type. The program should return the
final shipping fee and the estimated number of days for delivery.

1. Base Shipping Fee Table
Up to 50 km: $10.00.
From 51 km to 200 km: $20.00.
Above 200 km: $20.00 + $0.50 per additional km.

2. Business Rules (the "Real World")
Free Shipping: If the purchase value is greater than $250.00, shipping is
free (regardless of distance), except if the distance is greater than
500 km.

Customer Category:
Regular Customer: No benefits.
VIP Customer: 50% discount on the shipping fee and delivery is always
2 days faster than standard.

Delivery Deadline:
Every 100 km of distance adds 1 day to the deadline (minimum of 1 day).

Why is this good practice?
In real life, code is rarely a straight line. The challenge here is:

Avoiding "Spaghetti Code": If you just throw if/else statements around
without thinking, the code becomes impossible to read.

Exception Handling: What happens if the distance is negative? Or if the
purchase value is zero?

Extensibility: If tomorrow the boss asks to add a "Prime Customer" or
"International Shipping", is your code easy to change?

Example input and expected output:
Input: Purchase $300.00 | Distance 600 km | Type: Regular
Logic: Exceeded 500 km, so it loses free shipping. 600 km costs $220.00.
Output: Shipping: $220.00 | Deadline: 6 days.
"""

import math


def calculate_fee_and_delivery(purchase_value: float, distance: float, customer_type: str):
    # handling invalid values
    if purchase_value <= 0 or distance <= 0 or customer_type != "regular" and customer_type != "VIP":
        print("Invalid values!")
        return

    # delivery time that will serve as the base for the other business rules
    delivery_time = calculate_delivery_time(distance)

    # free shipping
    if purchase_value >= 1000:
        shipping_fee = 0
    elif purchase_value >= 250 and distance <= 500:
        shipping_fee = 0
    elif customer_type == "VIP" and purchase_value >= 250:
        shipping_fee = 0
    else:
        # shipping fee that will serve as the base for the other business rules
        shipping_fee = calculate_fee(distance)

    # handling VIP customer perks
    if customer_type == "VIP":
        # if shipping isn't already free
        if shipping_fee != 0:
            # 50% discount on the fee
            shipping_fee = shipping_fee / 2
        # the minimum deadline must be 1 day, whether VIP or not
        if delivery_time <= 2:
            delivery_time = 1
        else:
            delivery_time = delivery_time - 2
    return f"Shipping: ${shipping_fee:.2f} | Deadline: {delivery_time} days"


def calculate_fee(distance):
    if distance <= 50:
        return 10.0
    if distance > 50 and distance <= 200:
        return 20.0
    if distance > 200:
        over_200 = (distance - 200) * 0.5 + 20.0
        return over_200


def calculate_delivery_time(distance):
    # minimum of 1 day regardless of distance
    if distance < 100:
        return 1
    else:
        delivery_time = math.ceil(distance / 100)
        return delivery_time


# --- Test Cases to Validate Your Logic ---

# 1. Regular customer, short distance (should charge the base fee)
test1 = calculate_fee_and_delivery(100.0, 30, "regular")
# Expected: Shipping $10.00, Deadline 1 day

# 2. Regular customer, medium distance (between 51 and 200km)
test2 = calculate_fee_and_delivery(150.0, 147, "regular")
# Expected: Shipping $20.00, Deadline 2 days (due to rounding)

# 3. Regular customer, long distance (fee per additional km)
test3 = calculate_fee_and_delivery(100.0, 250, "regular")
# Expected: 250km -> $20 (base) + $25 (50 additional km) = $45.00
# Deadline: 3 days

# 4. Free shipping (purchase > 250 and distance < 500)
test4 = calculate_fee_and_delivery(350.0, 400, "regular")
# Expected: Shipping $0.00, Deadline 4 days

# 5. Loss of free shipping due to distance (purchase > 250 but distance > 500)
test5 = calculate_fee_and_delivery(300.0, 600, "regular")
# Expected: 600km -> $20 (base) + $200 (400 additional km) = $220.00
# Deadline: 6 days

# 6. VIP customer (50% discount and faster delivery)
test6 = calculate_fee_and_delivery(100.0, 250, "VIP")
# Expected: Shipping $22.50 (half of $45), Deadline 1 day (3 days - 2 bonus days)
# Tip: The minimum deadline should always be 1 day, don't let it become zero or negative!

results = [test1, test2, test3, test4, test5, test6]

for i, res in enumerate(results, 1):
    print(f"Test {i}: {res}")

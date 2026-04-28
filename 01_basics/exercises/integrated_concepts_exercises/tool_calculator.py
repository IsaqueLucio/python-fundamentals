"""
Challenge 4: Toll Calculator
File: 14_toll_calculator.py

Rules:
1. Create a loop that asks for the vehicle type: "1. Car | 2. Motorcycle | 3. Truck | 0. End day".
2. If the user enters 0, break the loop.
3. Base prices: Car = 10.0, Motorcycle = 5.0, Truck = 20.0.
4. Before charging, ask: "Do you have an auto-pay tag? (y/n)".
5. If the answer is "y", apply a 10% discount (multiply by 0.90) using a conditional statement.
6. Print the final amount to be paid, properly formatted.
7. The loop must continue asking for vehicles until the day is ended with 0.
"""

while True:
    print("\n--- | Tool Calculator | ---\n")
    print("Choose one of the options below: ")
    vehicle_option = input(f"1. Car\n"
                            "2. Motorcycle\n"
                            "3. Truck\n"
                            "0. End day\n")
    
    if vehicle_option != "1" and vehicle_option != "2" and vehicle_option != "3" and vehicle_option != "0":
        print("Only the option 1,2,3 and 0 are avaliable.")
        continue

    if vehicle_option == "0":
        print("\nSuccess, leaving the program.")
        break

    user_input = input("\nDo you have an auto-pay tag? (y/n)\n").lower()
    if user_input != "y" and user_input != "n":
        print(f"Only 'y' or 'n' is accepted.")
        continue
    
    has_autoPay_tag = ""
    if user_input == "y":
        has_autoPay_tag = True
    else: 
        has_autoPay_tag = False

    if vehicle_option == "1":
        car = 10.0
        if has_autoPay_tag:
            car = car-(car/10) 
            print("\nYou are driving a car, so the taxe is R$ 10,00.")
            print(f"But how do you have the auto-pay tag, you gain a 10% discount.")
            print(f"Therefore, the amount that must be paid is: R$ {car}")
        else:
            print("\nYou are driving a car, so the taxe is R$ 10,00.")
            print("You don't have the auto-pay tag, then you don't get the discount of 10%.")
            print(f"Therefore, the amount that must be paid is: R$ {car}")
    elif vehicle_option == "2":
        motorcycle = 5.0
        if has_autoPay_tag:
            motorcycle = motorcycle-(motorcycle/10) 
            print("\nYou are driving a motorcycle, so the taxe is R$ 5,00.")
            print(f"But how do you have the auto-pay tag, you gain a 10% discount.")
            print(f"Therefore, the amount that must be paid is: R$ {motorcycle}")
        else:
            print("\nYou are driving a motorcycle, so the taxe is R$ 5,00.")
            print("You don't have the auto-pay tag, then you don't get the discount of 10%.")
            print(f"Therefore, the amount that must be paid is: R$ {motorcycle}")
    elif vehicle_option == "3":
        truck = 20.0
        if has_autoPay_tag:
            truck = truck-(truck/10) 
            print("\nYou are driving a truck, so the taxe is R$ 20,00.")
            print(f"But how do you have the auto-pay tag, you gain a 10% discount.")
            print(f"Therefore, the amount that must be paid is: R$ {truck}")
        else:
            print("\nYou are driving a truck, so the taxe is R$ 20,00.")
            print("You don't have the auto-pay tag, then you don't get the discount of 10%.")
            print(f"Therefore, the amount that must be paid is: R$ {truck}")
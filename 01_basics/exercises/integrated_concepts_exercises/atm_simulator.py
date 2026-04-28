"""
Challenge 1: Simple ATM Simulator
File: 11_atm_simulator.py

Rules:
1. Start with a 'balance' variable set to 1000.0.
2. Create an infinite loop (while True).
3. Inside the loop, display a menu: "1. View Balance | 2. Withdraw | 3. Deposit | 4. Exit".
4. Ask the user to choose an option.
5. If option 1: print the current balance.
6. If option 2: ask for the withdrawal amount (convert to float). If the amount is greater than the balance, print an "Insufficient funds" error. If valid, subtract from the balance and display the new balance.
7. If option 3: ask for the deposit amount (convert to float). If the amount is less than or equal to 0, print an error message. If valid, add to the balance and display the new balance.
8. If option 4: use the 'break' command to exit the loop and end the program.
"""

# 1. Initialize the balance variable
balance = 1000.0

# 2. Creating the loop
while True:
    option = input("1. View Balance\n"
                    "2. Withdraw\n"
                    "3. Deposit\n"
                    "4. Exit\n")
    if option != "1" and option != "2" and option != "3" and option != "4":
        print("Only the option 1,2,3 and 4 are avaliable.")
    elif option == "1":
        print(f"The actual balance is: R${balance}")
    elif option == "2":
        withdrawn_value = float(input("Insert the value that you will withdrawn: "))
        if withdrawn_value <= 0.0:
            print("You cannt withdrawn a value less or equal to 0.")
        elif withdrawn_value > balance:
            print("Insuficient founds!")
        else:
            balance -= withdrawn_value
            print(f"Sucess, you got the total of R${withdrawn_value} from your balance. New balance: R${balance}")
    elif option == "3":
        deposited_value = float(input("Insert the value that you will deposited: "))
        if deposited_value <= 0.0:
            print("You cannot deposit a value less or equal to 0.")
            print(f"Success! You deposited R${deposited_value}. New balance: R${balance}")
        else:
            balance += deposited_value
    elif option == "4":
        print("Success, leaving the program.")
        break
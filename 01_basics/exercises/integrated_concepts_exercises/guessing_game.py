"""
Challenge 2: Secret Number Guessing Game
File: 12_guessing_game.py

Rules:
1. Define a 'secret_number' variable with the value 42 and an 'attempts' variable set to 0.
2. Create a 'while' loop that runs as long as attempts are less than 5.
3. Ask the user for a guess (convert to int).
4. Add 1 to the attempts variable.
5. If the guess equals the secret number, print "You win!" and use 'break'.
6. If the guess is higher, print "Try a lower number".
7. If the guess is lower, print "Try a higher number".
8. If the loop finishes without breaking (check if attempts reached 5 outside the loop), print "Game Over".
"""

# 1. Define the secret number and attempts variable
secret_number = 42
attempts = 0
# 2. Creating the while loop
while attempts < 5:
    # 3. Asking the user for a guess
    num = int(input("Guess the secret number: "))
    # 4. Adding 1 to the attempts variable
    attempts += 1
    # 5. If the guess equals the secret number
    if num == secret_number:
        # printing "You win!"
        print("You win!!!")
        # and using 'break'
        break
    # 6. If the guess is higher
    elif num > secret_number:
        # printing "Try a lower number"
        print("Try a lower number")
    # 7. If the guess is lower
    else:
        # print "Try a higher number"
        print("Try a higher number")
# 8. If the loop finishes without breaking (check if attempts reached 5 outside the loop)
if attempts == 5:
    # printing "Game Over"
    print("Game Over.")
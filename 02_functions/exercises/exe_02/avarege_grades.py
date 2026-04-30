"""
Exercise 2.2: Dynamic Average Calculator (*args)
File: 05_average_grades.py

Rules:
1. Create a function called 'calculate_average' that uses '*args' to accept any number of grades.
2. Inside the function, calculate the average (sum of all grades divided by the length of the args tuple).
   Hint: use sum(args) and len(args).
3. Return the calculated average.
4. Call the function passing 3 grades, print the result.
5. Call the function again passing 5 grades, print the result.
"""

def calculate_avarege(*args):
    return sum(args)/len(args)

avarege_grades = calculate_avarege(8.5,6,9.8,5.9,7.5)
print(f"The avarege grade is: {avarege_grades:.2f}")
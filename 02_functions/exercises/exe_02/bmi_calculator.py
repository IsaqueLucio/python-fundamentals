"""
Exercise 2.1: BMI Calculator with Type Hinting
File: 04_bmi_calculator.py

Rules:
1. Create a function called 'calculate_bmi'.
2. Use Type Hinting to indicate that it receives 'weight' (float) and 'height' (float), and returns a 'float'.
3. The BMI formula is: weight / (height * height).
4. Return the calculated BMI.
5. Outside the function, call it, store the returned value in a variable, and print it formatted to 2 decimal places.
"""

def calculate_bmi(weight: float, height: float) -> float:
    return  weight/(height**2)

result = calculate_bmi(62.1, 1.66)
print(f"Your BMI is : {result:.2f}")

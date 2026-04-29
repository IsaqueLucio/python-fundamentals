"""
Exercise 1.3: Temperature Converter
File: 03_temp_converter.py

Rules:
1. Create a global variable 'standard_unit' with the value "Celsius".
2. Create a function called 'convert_to_fahrenheit' that takes a parameter 'celsius_temp'.
3. The formula is: (celsius_temp * 9/5) + 32.
4. Inside the function, print the result using the global variable to state the original unit.
   Example: "Converting 30 Celsius to Fahrenheit gives 86.0F".
5. Call the function with a test value.
"""

standard_unit = "Celsius"

def convert_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    print(f"Converting {celsius_temp}° Celsius to Fahrenheit gives {fahrenheit_temp}F.")

convert_to_fahrenheit(0)
convert_to_fahrenheit(30)
convert_to_fahrenheit(10)
convert_to_fahrenheit(24.8)
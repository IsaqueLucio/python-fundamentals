"""
Exercise 1: The Execution Guard
Main File: main.py
Dependencies to create in the same folder: string_utils.py

--- Rules for 'string_utils.py' ---
1. Create a function 'reverse_string(text: str) -> str' that returns the reversed text. (Hint: text[::-1]).
2. Create a function 'count_vowels(text: str) -> int' that counts and returns the number of vowels in the text.
3. At the bottom of 'string_utils.py', add the execution guard: if __name__ == "__main__":
4. Inside the guard block, write a print statement testing both functions (e.g., reversing "Python" and counting vowels in "Developer").
5. Run 'string_utils.py' directly to see your test print.

--- Rules for 'main.py' (This file) ---
1. Import the 'string_utils' module.
2. Run 'main.py'. You should NOT see the test prints from 'string_utils.py' (because of the guard!).
3. Call 'string_utils.reverse_string("Architecture")' and print the result.
"""

import string_utils

print(string_utils.reverse_string("Architecture"))
print(string_utils.count_vowels("Architecture"))


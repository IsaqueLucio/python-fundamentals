"""
Exercise 3: Chained Generator Pipeline
Main File: main.py

Rules:
1. Create a list of raw transaction numbers (some integers, some strings, some negative numbers):
   raw_transactions = [100, "-50", 200, "INVALID", -20, "300", 50, "-10"]

2. Generator 1 (The Parser): Create 'parse_to_int(data)'.
   - Loop through 'data'. Use a 'try/except ValueError' block to attempt converting each item to an int using 'int(item)'.
   - If successful, 'yield' the integer. If it fails (like "INVALID"), just pass/ignore it.

3. Generator 2 (The Filter): Create 'filter_positive(numbers)'.
   - Loop through 'numbers' (which will be the output of Generator 1!).
   - If the number is greater than 0, 'yield' it.

4. OUTSIDE the functions, chain them together!
   - parsed_gen = parse_to_int(raw_transactions)
   - positive_gen = filter_positive(parsed_gen)

5. Finally, use a for-loop on 'positive_gen' to print only the valid, positive transactions!
"""

raw_transactions = [100, "-50", 200, "INVALID", -20, "300", 50, "-10"]

def parse_to_int(database):
   for data in database:
      try:
         data_int = int(data)
         yield data_int
      except ValueError:
         pass
      finally:
         pass

def filter_positive(numbers):
   for num in numbers:
      if num > 0:
         yield num
      else:
         continue

parsed_gen = parse_to_int(raw_transactions)
positive_gen = filter_positive(parsed_gen)

for num in positive_gen:
   print(num)
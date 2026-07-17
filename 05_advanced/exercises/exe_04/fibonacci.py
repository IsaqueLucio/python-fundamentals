"""
Exercise 1: Infinite Fibonacci Generator
Main File: main.py

Rules:
1. Create a generator function called 'fibonacci_gen()'.
2. Inside the function, initialize two variables: a = 0 and b = 1.
3. Create an infinite loop using 'while True:'.
4. Inside the loop:
   - Use 'yield' to return the current value of 'a'.
   - Update 'a' and 'b' simultaneously to their next values: a, b = b, a + b
5. OUTSIDE the function, create an instance of the generator: fib = fibonacci_gen()
6. Use a standard 'for' loop combined with 'range(10)' and the 'next()' function to print the first 10 numbers of the sequence.
"""

def fibonacci_gen():
   a = 0
   b = 1
   while True:
      yield a
      a, b = b, a+b

fib = fibonacci_gen()

for i in range(10):
   print(next(fib))


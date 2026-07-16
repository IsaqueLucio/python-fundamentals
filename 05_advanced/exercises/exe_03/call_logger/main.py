"""
Exercise 1: The Call Logger
Main File: main.py

Rules:
1. Create a decorator function called 'log_call(func)'.
2. Inside 'log_call', create a 'wrapper(*args, **kwargs)' function.
3. In the wrapper:
   - Print a log message BEFORE the function runs: 
     f"[LOG] Calling function '{func.__name__}' with args: {args} and kwargs: {kwargs}"
   - Execute the original function and store its return value in a variable.
   - Print a log message AFTER the function runs: 
     f"[LOG] Function '{func.__name__}' completed. Returned: {result}"
   - Return the result.
4. Create a standalone function 'add_numbers(a: int, b: int) -> int' that returns a + b, and apply the @log_call decorator to it.
5. Create another function 'greet(name: str, greeting="Hello") -> str' that returns f"{greeting}, {name}!", and apply @log_call to it.
6. Test both functions at the bottom of the file and check the logs in the terminal!
"""
from log_call import log_call

@log_call
def add_numbers(a: int, b: int) -> int:
    return a+b 

@log_call
def greet(name: str, greeting="Hello") -> str:
    return f"{greeting}, {name}!"

add_numbers(2,7)
greet("Luke")
greet("Luke", greeting = "May the force be with you")
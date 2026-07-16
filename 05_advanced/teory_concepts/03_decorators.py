"""
Python Core - 05 Advanced
File: 03_decorators.py
Description: Understanding how decorators wrap functions to extend their behavior.
"""
import time

print("--- 1. Functions as First-Class Citizens ---")
# In Python, functions are just objects. You can pass them as arguments!

def say_hello(name):
    return f"Hello, {name}!"

def execute_function(func, arg):
    # We receive a function 'func' and call it inside here
    print("Executing the passed function...")
    return func(arg)

print(execute_function(say_hello, "Developer"))


print("\n--- 2. The Basic Decorator ---")
# A decorator is a function that receives another function, wraps it inside an inner function, 
# adds some new behavior, and returns the inner function.

def my_custom_decorator(func):
    def wrapper():
        print(">> Something is happening BEFORE the function is called.")
        func() # Calling the original function
        print(">> Something is happening AFTER the function is called.")
    return wrapper # We return the 'upgraded' inner function

# The @ syntax is syntactic sugar. 
# It automatically passes 'stand_alone_function' into 'my_custom_decorator'.
@my_custom_decorator
def stand_alone_function():
    print("I am a simple stand-alone function.")

# When we call it, we are actually calling the 'wrapper' from the decorator!
stand_alone_function()


print("\n--- 3. A Real-World Example: Execution Timer ---")
# To make decorators work with functions that take arguments, we use *args and **kwargs in the wrapper.

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the actual function and store its result
        result = func(*args, **kwargs) 
        
        end_time = time.time()
        print(f"[TIMER] Function '{func.__name__}' took {end_time - start_time:.4f} seconds to run.")
        
        # We must return the original result so the function doesn't lose its purpose
        return result 
    return wrapper

@timer_decorator
def heavy_computation(x):
    print(f"Calculating {x} squared a million times...")
    for _ in range(1_000_000):
        _ = x * x
    return "Heavy computation finished!"

print(heavy_computation(5))
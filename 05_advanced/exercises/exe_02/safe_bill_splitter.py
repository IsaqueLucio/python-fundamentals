"""
Exercise 1: Safe Bill Splitter
Main File: main.py

Rules:
1. Create a function called 'split_bill(total: float, people: int)'.
2. Inside the function, write a 'try' block that returns 'total / people'.
3. Still inside the function, catch the 'ZeroDivisionError' and return: "Error: You cannot split a bill with 0 people!"
4. Catch the 'TypeError' and return: "Error: Number of people must be a valid number!"
5. OUTSIDE the function, test the code by printing the results of:
   - split_bill(100.0, 2)       (Should succeed)
   - split_bill(100.0, 0)       (Should trigger ZeroDivisionError)
   - split_bill(100.0, "five")  (Should trigger TypeError)
"""

def split_bill(total: float, people: int) -> float:
    try:
        result = total/people
        return result
    except ZeroDivisionError:
        return "Error: You cannot split a bill with 0 people!"
    except TypeError:
        return "Error: Number of people must be a valid number!"
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
    finally:
        pass

print(split_bill(100.0, 2))
print(split_bill(100.0, 0))
print(split_bill(100.0, "five"))
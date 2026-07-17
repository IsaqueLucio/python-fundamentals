"""
Python Core - 05 Advanced
File: 04_generators.py
Description: Understanding Generators, the 'yield' keyword, and memory efficiency.
"""
import sys

print("--- 1. The Basic Generator: yield vs return ---")
# A standard function generates ALL values at once and stores them in memory.
def get_number_list():
    result = []
    for i in range(1, 4):
        result.append(i)
    return result

# A generator function yields ONE value at a time and pauses its state.
def get_number_generator():
    for i in range(1, 4):
        print(f"   [GEN] Calculating number {i}...")
        yield i
        print(f"   [GEN] Resuming after yielding {i}...")

print("Calling normal function:")
my_list = get_number_list()
print(f"List output: {my_list}\n")

print("Calling generator function:")
my_gen = get_number_generator()
print(f"Generator object created: {my_gen}")
# Notice that NO calculation happened yet! It only runs when we ask for the next item.

print("\nAsking for values one by one using next():")
val1 = next(my_gen)
print(f"Received: {val1}\n")

val2 = next(my_gen)
print(f"Received: {val2}\n")

val3 = next(my_gen)
print(f"Received: {val3}\n")

# If we call next(my_gen) a 4th time, Python raises a 'StopIteration' error!


print("--- 2. Generator Expressions (The Tuple Illusion) ---")
# You already know List Comprehensions with square brackets [x for x in ...].
# If you replace square brackets with parentheses (x for x in ...), you get a Generator Expression!

list_comp = [x * x for x in range(10)]
gen_expr = (x * x for x in range(10))

print(f"List comprehension: {list_comp}")
print(f"Generator expression: {gen_expr}")
print("To see the values of gen_expr, we can loop through it:")
for val in gen_expr:
    print(val, end=" ")
print("\n")


print("--- 3. Real-World Proof: Memory Efficiency ---")
# Let's compare the RAM memory size of a List vs a Generator for 1 MILLION numbers.

N = 1_000_000

# List: Allocates 1 million integers in RAM at once
massive_list = [i for i in range(N)]

# Generator: Only stores the recipe to generate the next number
massive_gen = (i for i in range(N))

list_size_bytes = sys.getsizeof(massive_list)
gen_size_bytes = sys.getsizeof(massive_gen)

print(f"Memory used by List (1M items):      {list_size_bytes:,} bytes (~{list_size_bytes / 1024 / 1024:.2f} MB)")
print(f"Memory used by Generator (1M items): {gen_size_bytes:,} bytes")
print(f"The Generator is around {list_size_bytes // gen_size_bytes:,} times lighter in memory!")
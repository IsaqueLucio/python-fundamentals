"""
Challenge: Two Sum

Given an array of integers and a target value, find the two numbers in the
array that add up to the target and return their indices and values.

Approach: brute-force with two nested loops, checking every possible pair
of elements until a pair whose sum matches the target is found.
"""


def two_sum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return f" Target number: {target}\nIndices of the numbers: {[i, j]} \n Numbers: {[array[i], array[j]]}"


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = two_sum(array, 9)
print(result)

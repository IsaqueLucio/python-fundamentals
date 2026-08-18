
"""
Challenge: Second Largest

Given an array of integers, find and return the second largest number in the array.

Approach: Single pass through the array, keeping track of the largest and second
largest values. As we iterate, we update these values whenever we find a number
larger than the current largest (shifting the largest to second) or larger than
the current second largest (but not equal to the largest).

Requirements:
- Handle arrays with duplicate values
- Return None if there are fewer than two distinct values
- Efficiently solve in O(n) time with a single iteration
"""

def second_largest(nums):
    largest = None
    second = None

    for num in nums:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

arrays = [1, 3, 4, 5, 6, 9, 7, 8, 9, 10]
print(second_largest(arrays))
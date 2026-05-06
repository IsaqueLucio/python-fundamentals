"""
Exercise 3: Financial Summary
File: 06_financial_summary.py

Rules:
1. Create a function called 'analyze_revenues' that receives a list of floats called 'revenues'.
2. Inside the function, calculate the highest revenue (use the max() function), 
the lowest revenue (use the min() function), and the average revenue (sum / length).
3. Return all three calculated values separated by commas (this automatically creates a tuple in Python).
4. Outside the function, call it passing a list of numbers (e.g., [1500.50, 3200.00, 800.75, 5000.00]).
5. Use Tuple Unpacking to capture the returned values directly into three variables: 'highest', 'lowest', and 'avg'.
6. Print the three values formatted.
"""

def analyze_revenues(revenues):
    maxRevenues = max(revenues)
    minRevenues = min(revenues)
    avg = sum(revenues)/len(revenues)
    return (maxRevenues,minRevenues,avg)

nums = [500.50, 3200.00, 800.75, 5000.00]
revenues = analyze_revenues(nums)
print(f"Revenues values: {revenues}")
highest, lowest ,avg = revenues
print(f"The highest value of the revenues is: {highest}\n"
      f"The lowest value of the revenues is: {lowest}\n"
      f"The avarege value of the revenues is: {avg:.2f}")


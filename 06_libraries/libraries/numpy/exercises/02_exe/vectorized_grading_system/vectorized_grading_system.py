"""
Python Core - 06 Libraries (numpy)
Exercise 2: The Vectorized Grading System (Intermediate - Logic & Interpretation)
Folder: 02_vectorized_grading_system/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. You are processing the final exam scores of 10 university students:
   scores = np.array([45, 82, 95, 33, 67, 78, 55, 89, 91, 72])
3. Binary Classification (np.where):
   - The passing grade is 60.
   - Use 'np.where' to create an array called 'pass_fail_status' containing the string "PASS" if the score is >= 60, or "FAIL" if it is < 60.
   - Print the resulting array.
4. Complex Classification (np.select):
   - Now, the university wants detailed letter grades!
   - Define a list of conditions:
     * Score >= 90
     * Score >= 70 and Score < 90
     * Score >= 50 and Score < 70
     * Score < 50
   - Define the corresponding list of choices: ["A", "B", "C", "F"]
   - Use 'np.select' to apply these conditions to the 'scores' array and store the result in 'letter_grades'.
   - Print the final 'letter_grades' array!
"""

import numpy as np

scores = np.array([45, 82, 95, 33, 67, 78, 55, 89, 91, 72])
pass_fail_status = np.where(scores >= 60, "PASS", "FAIL")
print(f"RESULTS: {pass_fail_status}.")

conditions = [
    scores >= 90, 
    (scores >= 70) & (scores < 90), 
    (scores >= 50) & (scores < 70), 
    scores < 50
    ]
choices = ["A", "B", "C", "F"]
letter_grades = np.select(conditions, choices, default="UK")
print(f"Final grades: {letter_grades}.")
"""
Challenge 2: HR Data Processing
File: 11_employee_filter.py

Rules:
1. Create a list of dictionaries representing employees:
   employees = [
       {"name": "Ana", "salary": 4500},
       {"name": "Bob", "salary": 6000},
       {"name": "Carlos", "salary": 3800},
       {"name": "Diana", "salary": 7500}
   ]
2. Task 1 (Filter): Use 'filter()' and a lambda to create a list of ONLY employees earning more than 5000.
3. Task 2 (Map): Use 'map()' and a lambda on the filtered list to extract ONLY the names of those high-earning employees.
4. Print the final list of names. (Expected output: ['Bob', 'Diana'])
"""

employees = [
       {"name": "Ana", "salary": 4500},
       {"name": "Bob", "salary": 6000},
       {"name": "Carlos", "salary": 3800},
       {"name": "Diana", "salary": 7500}
   ]

task_01 = list(filter(lambda salary: salary['salary'] > 5000, employees))
print(task_01)
task_02 = list(map(lambda name : name['name'],task_01))
print(task_02)

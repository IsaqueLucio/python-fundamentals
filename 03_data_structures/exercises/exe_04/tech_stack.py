"""
Exercise 3: Tech Stack Analyzer
File: 12_tech_stack.py

Rules:
1. Create a set called 'project_a_stack' with: {"Python", "Docker", "PostgreSQL", "Redis"}
2. Create a set called 'project_b_stack' with: {"Node.js", "Docker", "MongoDB", "Redis"}
3. Use .intersection() to find which technologies are used in BOTH projects and print the result.
4. Use .union() to get a list of ALL unique technologies used across both projects and print the result.
5. Use .difference() to find the technologies that are ONLY in project A (not in project B) and print the result.
"""

project_a_stack = {"Python", "Docker", "PostgreSQL", "Redis"}
project_b_stack = {"Node.js", "Docker", "MongoDB", "Redis"}

intersection = project_a_stack.intersection(project_b_stack)
print(intersection)
unique_tecnologies = project_a_stack.union(project_b_stack)
print(unique_tecnologies)
tecnologies_in_only_project_a = project_a_stack.difference(project_b_stack)
print(tecnologies_in_only_project_a)
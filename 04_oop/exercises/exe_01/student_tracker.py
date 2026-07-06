"""
Exercise 3: Student Grade Tracker
File: 04_student_tracker.py

Rules:
1. Create a class called 'Student'.
2. The __init__ method takes 'name' (str) and 'course' (str).
3. Initialize an empty list attribute called 'grades' (self.grades = []).
4. Create a method 'add_grade(self, grade)'. It should append the grade to 'self.grades' and print a confirmation message.
5. Create a method 'get_average(self)'. 
   - If the 'grades' list is empty, return 0.
   - Otherwise, calculate and return the average of the grades (sum / len).
6. Create a Student object.
7. Add three grades (e.g., 8.0, 9.5, 7.5) using the 'add_grade' method.
8. Call 'get_average()', save the result in a variable, and print it formatted to 2 decimal places.
"""

class Student:

    def __init__(self, name: str, course: str):
        self.name = name
        self.course = course
        self.grades = []
    
    def add_grade(self, grade: float):
        self.grades.append(grade)
        print("Done! Note added to the student's record.")

    def get_average(self):
        if not self.grades:
            return 0
        else:
            average = sum(self.grades)/len(self.grades)
            return average
        
student = Student("Mike", "Medicine")
student.add_grade(8.0)
student.add_grade(9.5)
student.add_grade(7.5)

student_average = student.get_avarege()

print(f"The avarege grade of the student {student.name} is {student_average:.2f}")
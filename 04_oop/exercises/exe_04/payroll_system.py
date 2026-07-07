"""
Exercise 3: Payroll System
File: 15_payroll_system.py

Rules:
1. Import the necessary tools from 'abc'.
2. Create an abstract class 'Employee(ABC)'.
3. Add an __init__ taking 'name' (str).
4. Create a normal method 'get_name(self)' that returns the name.
5. Create an abstract method 'calculate_salary(self) -> float'.
6. Create a concrete class 'FullTimeEmployee' inheriting from 'Employee'.
   - Its __init__ should take 'name' and 'monthly_salary'. Use super() for the name.
   - Implement 'calculate_salary' to simply return the 'monthly_salary'.
7. Create a concrete class 'HourlyEmployee' inheriting from 'Employee'.
   - Its __init__ should take 'name', 'hours_worked', and 'hourly_rate'. Use super() for the name.
   - Implement 'calculate_salary' to return 'hours_worked * hourly_rate'.
8. Create one FullTimeEmployee and one HourlyEmployee.
9. Print their names (using the inherited method) and their calculated salaries.
"""

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    @abstractmethod
    def calculate_salary(self) -> float:
        pass

class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary: float):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary
    
class HourlyEmployee(Employee):

    def __init__(self, name, hours_worked: float, hourly_rate: float):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
obj1 = FullTimeEmployee("Mike", 4000.95)
obj2 = HourlyEmployee("Veronica", 50, 40.37)
print(f"{obj1.get_name()} \n {obj1.calculate_salary()}")
print(f"{obj2.get_name()} \n {obj2.calculate_salary():.2f}")
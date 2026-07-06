"""
Python Core - 04 Object-Oriented Programming
File: 09_inheritance.py
Description: Parent classes, Child classes, and the super() function.
"""

print("--- 1. The Parent Class (Superclass) ---")
# This is the base blueprint. It has the generic data every employee shares.
class Employee:
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        return f"{self.name} earns ${self.base_salary}/month."

    def calculate_bonus(self):
        # Generic employees get a standard 10% bonus
        return self.base_salary * 0.10


print("\n--- 2. The Child Classes (Subclasses) ---")
# To inherit, we put the Parent class name inside parentheses ()
class Manager(Employee):
    
    # The Manager has an extra attribute: department
    def __init__(self, name: str, base_salary: float, department: str):
        # super() calls the Parent's __init__ to handle the shared attributes
        super().__init__(name, base_salary)
        
        # Now we only handle the specific attribute for this child
        self.department = department

    # Method Overriding: We can rewrite a parent's method to change its behavior
    def calculate_bonus(self):
        # Managers get a 20% bonus instead of 10%
        return self.base_salary * 0.20

class Intern(Employee):
    # If we don't write an __init__ here, Python automatically uses the Parent's __init__!
    
    def calculate_bonus(self):
        # Interns don't get bonuses
        return 0


print("\n--- 3. Testing the Inheritance ---")
emp = Employee("Alice", 3000)
mgr = Manager("Bob", 6000, "IT")
intn = Intern("Charlie", 1000)

# All of them can use the get_details() method inherited from Employee!
print(f"Employee details: {emp.get_details()}")
print(f"Manager details: {mgr.get_details()} (Dept: {mgr.department})")
print(f"Intern details: {intn.get_details()}")

# But their overridden methods calculate bonuses differently
print(f"\nBonuses -> Alice: ${emp.calculate_bonus()} | Bob: ${mgr.calculate_bonus()} | Charlie: ${intn.calculate_bonus()}")
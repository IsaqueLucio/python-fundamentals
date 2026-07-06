"""
Python Core - 04 Object-Oriented Programming
File: 01_classes_objects.py
Description: Creating classes, the __init__ constructor, and instance methods.
"""

print("--- 1. Defining a Class (The Blueprint) ---")
# Class names always use PascalCase (Capitalize every word, no underscores)
class Developer:
    
    # The __init__ method is the Constructor. 
    # It runs automatically every time we create a new object from this class.
    # 'self' represents the specific object being created (like 'this' in Java).
    def __init__(self, name: str, role: str, salary: float):
        self.name = name       # "This object's name will be the name passed in"
        self.role = role       
        self.salary = salary
        self.skills = []       # We can also define default attributes!

    # This is an Instance Method (an action the object can perform).
    # It MUST always have 'self' as the first parameter so it knows whose data to use.
    def learn_skill(self, new_skill: str):
        self.skills.append(new_skill)
        print(f"{self.name} just learned {new_skill}!")

    def show_profile(self):
        print(f"[{self.role}] {self.name} | Salary: ${self.salary} | Skills: {self.skills}")


print("\n--- 2. Creating Objects (Building the Houses) ---")
# We create an object by calling the Class name as if it were a function.
# We DO NOT pass 'self'. Python handles 'self' automatically in the background.
dev1 = Developer("Alice", "Backend Engineer", 8500.00)
dev2 = Developer("Bob", "Frontend Developer", 7200.50)

# Accessing attributes directly using the dot notation (.)
print(f"Dev 1 Name: {dev1.name}")
print(f"Dev 2 Role: {dev2.role}")


print("\n--- 3. Using Methods (Making the objects do things) ---")
# When dev1 calls a method, 'self' becomes dev1.
dev1.learn_skill("Python")
dev1.learn_skill("Docker")

# When dev2 calls a method, 'self' becomes dev2.
dev2.learn_skill("React")

# Let's see the final state of each independent object
print("\nFinal Profiles:")
dev1.show_profile()
dev2.show_profile()
"""
Exercise 1: Notification System
File: 13_notification_system.py

Rules:
1. Import ABC and abstractmethod from the 'abc' module.
2. Create an abstract class called 'Notifier' that inherits from ABC.
3. Define an abstract method called 'send(self, message: str) -> str'. Use 'pass' in the body.
4. Create a concrete class 'EmailNotifier' inheriting from 'Notifier'.
   - Implement the 'send' method to return: "Sending Email: [message]"
5. Create a concrete class 'SMSNotifier' inheriting from 'Notifier'.
   - Implement the 'send' method to return: "Sending SMS: [message]"
6. Create an object of EmailNotifier and an object of SMSNotifier.
7. Call the 'send' method on both objects with a test message and print the results.
8. (Optional test): Try to create an object directly from 'Notifier' to see the TypeError in action, then comment it out.
"""

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotifier(Notifier):

    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotifier(Notifier):

    def send(self, message):
        return f"Sending SMS: {message}"

obj1 = EmailNotifier()
obj2 = SMSNotifier()
print(obj1.send("EmailNotifier test."))
print(obj2.send("SMSNotifier test."))

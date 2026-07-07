"""
Exercise 2: Mass Notifier
File: 17_mass_notifier.py

Rules:
1. Create three separate classes: 'EmailAlert', 'SMSAlert', and 'PushAlert'.
2. Each class must have a method called 'send_alert(self, message: str)'.
   - EmailAlert should print: "Email sent: [message]"
   - SMSAlert should print: "SMS sent: [message]"
   - PushAlert should print: "Push Notification sent: [message]"
3. Create a list called 'notification_channels' containing one instance of each class.
4. Write a 'for' loop that iterates over 'notification_channels'.
5. Inside the loop, call 'send_alert("System goes down in 5 minutes!")' on each object.
"""

class EmailNotifier:

    def send(self, message) -> str:
        return f"Sending Email: {message}"

class SMSNotifier:

    def send(self, message) -> str:
        return f"Sending SMS: {message}"
    
class PushAlert:

    def send(self, message) -> str:
        return f"Push Notification sent: {message}"
    
notification_channels = [EmailNotifier(), SMSNotifier(), PushAlert()]

for type_message in notification_channels:
    print(type_message.send("Hello World"))
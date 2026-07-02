"""
Final Challenge 4: Event Check-in System
File: 16_event_checkin.py

Rules:
1. Create a dictionary representing an event:
   event_data = {
       "event_name": "Python Conference",
       "registered_emails": {"alice@email.com", "bob@email.com", "charlie@email.com", "diana@email.com"},
       "actual_checkins": [
           ("alice@email.com", "09:00 AM"),
           ("charlie@email.com", "09:15 AM")
       ]
   }
2. Extract the 'registered_emails' set into a variable.
3. Use a List Comprehension or a loop to create a NEW SET containing ONLY the emails from the 'actual_checkins' list of tuples.
   (Hint: Loop through the list, unpack the tuple, and add the email to the new set).
4. Use a Set operation to find the "no-shows" (people who are in the registered set but NOT in the checked-in set).
5. Print a formatted summary: 
   "Event: [name] | Total No-shows: [number_of_no_shows] | Missing: [no_shows_set]"
"""


"""
Challenge: Hours to Seconds

Convert a time string in "HH:MM:SS" format into the total number of
seconds it represents.
"""


def hours_to_seconds(time="01:00:00"):
    time_parts = time.split(":")
    hours_in_seconds = int(time_parts[0]) * 3600
    minutes_in_seconds = int(time_parts[1]) * 60
    total_seconds = hours_in_seconds + minutes_in_seconds + int(time_parts[2])
    return total_seconds

print(hours_to_seconds("01:00:00"))
print(hours_to_seconds("00:01:00"))
print(hours_to_seconds("02:30:15"))
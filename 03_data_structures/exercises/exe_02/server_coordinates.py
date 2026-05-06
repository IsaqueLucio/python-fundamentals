"""
Exercise 1: Server Coordinates
File: 04_server_coordinates.py

Rules:
1. Create a tuple called 'server_location' with the following data: (40.7128, -74.0060, "New York", "Active").
2. Use Tuple Unpacking to extract these values into four separate variables: 'lat', 'lon', 'city', and 'status'.
3. Print a formatted string using the unpacked variables:
   "Server in [city] is [status]. Coordinates: [lat], [lon]"
"""

server_location = (40.7128, -74.0060, "New York", "Active")
lat,lon,city,status = server_location
print(f"Server in {city} is {status}. Coordinates: {lat}, {lon}")
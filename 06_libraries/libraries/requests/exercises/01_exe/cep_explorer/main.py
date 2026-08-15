"""
Python Core - 06 Libraries
Module: requests
Exercise 01: CEP Explorer (Easy)
File: main.py

Rules:
1. Import the 'requests' module.
2. Define a variable 'url' with the endpoint for the postal code of downtown São Paulo: 
   url = "https://brasilapi.com.br/api/cep/v1/01001000"
3. Make a GET request to this URL using 'requests.get()'.
4. Print the 'status_code' of the response to ensure it is 200.
5. Convert the response into a Python dictionary using '.json()'.
6. Print a formatted message showing the following fields extracted from the dictionary:
   - State ('state')
   - City ('city')
   - Neighborhood ('neighborhood')
   - Street ('street')
"""

import requests

url = "https://brasilapi.com.br/api/cep/v1/01001000"

response = requests.get(url)

print(f"The status code of the GET of the url {url} is: {response.status_code}")
cep_data = response.json()
print(f"About the CEP {cep_data['cep']}:\n"
      f"State : {cep_data['state']}\n"
      f"City: {cep_data['city']}\n"
      f"Neighborhood: {cep_data['neighborhood']}\n"
      f"Street: {cep_data['street']}")
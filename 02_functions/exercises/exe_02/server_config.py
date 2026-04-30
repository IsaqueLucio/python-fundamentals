"""
Exercise 2.3: Server Configurator (**kwargs)
File: 06_server_config.py

Rules:
1. Create a function called 'configure_server' that takes 'server_name' as a standard parameter, and '**configs' for dynamic settings.
2. The function should print "Configuring server: [server_name]".
3. Loop through the '**configs' dictionary using .items() and print each key-value pair.
   Example: "- Os: Ubuntu", "- Ram: 16GB".
4. Call the function passing a server name and at least 3 dynamic named arguments (e.g., os="Linux", ram="32GB", region="US-East").
"""

def configure_server(server_name, **configs):
    print(f"Os: {server_name}\nConfigs: ")
    for key, value in configs.items():
        print(f" - {key.capitalize()}: {value}")

configure_server("Ubuntu",ram="16GB",rom="130GB",processor="Intel I5 12550HX",GPU ="RTX 3050")
print("")
configure_server("Windows",ram="32GB",rom="512GB",processor="Intel I7 14550HX",GPU="RTX 4060")

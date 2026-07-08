"""
Exercise 3: Computer Aggregation & Composition
Main File: main.py
Dependencies to create in the same folder: processor.py, monitor.py, computer.py

--- Rules for 'processor.py' ---
1. Create a class 'Processor' with an __init__ taking 'model' (str) and 'cores' (int).

--- Rules for 'monitor.py' ---
1. Create a class 'Monitor' with an __init__ taking 'brand' (str) and 'resolution' (str).

--- Rules for 'computer.py' ---
1. Import both 'Processor' and 'Monitor' classes.
2. Create a class 'Computer'.
3. The __init__ takes 'cpu_model' (str) and 'cpu_cores' (int). 
   - COMPOSITION: Inside __init__, use these parameters to create a Processor object and save it in 'self.processor'.
   - Also inside __init__, set 'self.monitor = None' (The computer starts without a monitor).
4. Create a method 'plug_monitor(self, monitor: Monitor)'. 
   - AGGREGATION: This method receives an external Monitor object and assigns it to 'self.monitor'.
5. Create a method 'show_specs(self)'. 
   - It should print the Processor model and cores.
   - If 'self.monitor' is not None, print the Monitor brand and resolution.
   - If 'self.monitor' is None, print "No monitor connected."

--- Rules for 'main.py' (This file) ---
1. Import 'Computer' and 'Monitor'.
2. Create a Computer object.
3. Call 'show_specs()' (It should report the CPU and say no monitor).
4. Create a Monitor object independently.
5. Call 'plug_monitor()' passing your Monitor object.
6. Call 'show_specs()' again to see the fully assembled setup.
"""

from computer import Computer
from monitor import Monitor

pc = Computer("I9 14990K", 24)
print(pc.show_specs())
monitor = Monitor("AOC", "2560x1440")
pc.plug_monitor(monitor)
print(pc.show_specs())
pc.unplug_monitor()
print(pc.show_specs())

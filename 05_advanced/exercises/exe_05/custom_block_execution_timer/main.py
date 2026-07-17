"""
Exercise 3: Custom Block Execution Timer
Main File: main.py

Rules:
1. Import 'time'.
2. Create a class named 'BlockTimer'.
3. In the '__init__(self, block_name: str)' method, save 'block_name' to an attribute and initialize 'self.start_time = 0.0'.
4. Implement the '__enter__(self)' method:
   - Record the current time using 'time.time()' in 'self.start_time'.
   - Print: f"[TIMER] Starting execution of block '{self.block_name}'..."
   - Return 'self'.
5. Implement the '__exit__(self, exc_type, exc_val, exc_tb)' method:
   - Calculate the elapsed time: elapsed = time.time() - self.start_time
   - Print: f"[TIMER] Block '{self.block_name}' finished in {elapsed:.4f} seconds.\n"
   - Return False (so any exceptions inside the block are not suppressed).
6. OUTSIDE the class, test your custom Context Manager using a 'with' block:
   with BlockTimer("Heavy Loop Simulation"):
       # Simulate heavy work by looping 5 million times
       total = sum(i for i in range(5_000_000))
       print(f"Loop calculation complete. Total: {total}")
7. Run the code and watch the automatic start and exit messages wrap around the execution block!
"""

from block_timer import BlockTimer

with BlockTimer("Heavy Loop Simulation"):
       # Simulate heavy work by looping 5 million times
       total = sum(i for i in range(5_000_000))
       print(f"Loop calculation complete. Total: {total}")
   

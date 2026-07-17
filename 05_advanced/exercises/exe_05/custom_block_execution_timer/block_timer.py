import time

class BlockTimer:
   def __init__(self, block_name: str):
      self.block_name = block_name
      self.start_time = 0.0
   
   def __enter__(self):
      self.start_time = time.time()
      print(f"[TIMER] Starting execution of block '{self.block_name}'...")
      return self
   
   def __exit__(self, exc_type, exc_val, exc_tb):
      elapsed = time.time() - self.start_time
      print(f"[TIMER] Block '{self.block_name}' finished in {elapsed:.4f} seconds.\n")
      return False


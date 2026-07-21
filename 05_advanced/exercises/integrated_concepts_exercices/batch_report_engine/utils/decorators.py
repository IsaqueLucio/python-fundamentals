from datetime import datetime

def audit_log(operation_name: str):
   def audit_log_decorator(func):
      def wrapper(*args, **kwargs):
        start_time =  datetime.now()
        print(f"Starting operation at [{start_time}]...")
        print(f"Executing the operation [{operation_name}]...")
        try:
         return func(*args, **kwargs)
        finally:
         end_time = datetime.now()
         print(f"Completing the operation at [{end_time}]...")
         final_time = end_time - start_time
         print(f"[TIMER] The function '{func.__name__}' started at {start_time} and finished at {end_time}, taking {final_time} seconds to execute the operation [{operation_name}].")
      return wrapper
   return audit_log_decorator
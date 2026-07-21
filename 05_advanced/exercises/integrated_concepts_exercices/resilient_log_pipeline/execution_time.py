import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time =  time.time()
        func(*args, **kwargs)
        end_time = time.time()
        final_time = end_time - start_time
        print(f"[TIMER] Function '{func.__name__}' took {final_time:.4f} seconds to run.")
        return final_time
    return wrapper
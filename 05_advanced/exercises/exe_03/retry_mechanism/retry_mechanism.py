def retry_three_times(func):
    def wrapper(*args,**kwargs):
        for attempt in range(1, 4):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[WARNING] Attempt {attempt} failed with error: '{e}'. Retrying...")
                if attempt == 3:
                    print("[ERROR] Function failed after 3 attempts.")
                    return None
    return wrapper    

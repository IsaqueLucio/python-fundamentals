def retry_on_network_error(func):
    def wrapper(*args,**kwargs):
        for attempt in range(1, 4):
            try:
                return func(*args, **kwargs)
            except ConnectionError as e:
                print(f"[WARNING] Attempt {attempt} failed with error: '{e}'. Retrying...")
                if attempt == 3:
                    raise
    return wrapper  
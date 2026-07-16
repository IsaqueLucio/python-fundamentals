def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(     f"[LOG] Function '{func.__name__}' completed. Returned: {result}")
        return result   
    return wrapper
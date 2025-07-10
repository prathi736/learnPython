import time

# creation of decorator (function ke ander function)
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} is ran in {end-start} time")
        # __name__ -> gives internal details in python
        return result
    return wrapper

# applied decorator
@timer
def example_function(n):
    time.sleep(n)

example_function(3)
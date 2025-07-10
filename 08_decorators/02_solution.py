
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Function Name: {func.__name__}. Args: {args_value} and Kwargs: {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hi")

@debug #ek tarika ka toll hai road(means function) par
def greet(name, greeting="Hello"):
    print(f"{greeting}: {name}")

hello()
greet("Billu", greeting="Hey")

# Very Different question for learning concepts of cache memory
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b

print(long_running_function(6,7))
print(long_running_function(6,7))
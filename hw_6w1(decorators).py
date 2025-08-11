import random
import time

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def retry_decor(retries):
    def actual_decor(func):
        def wrapper():
            for i in range(retries):
                try:
                    return func()
                except Exception as e:
                    print(f'Try №{i + 1} failed: {e}')
            print('All tries are failed')
        return wrapper
    return actual_decor

@retry_decor(3)
def unstable():
    if random.random() < 0.7:
        raise ValueError("Random failure occurred!")
    print("Function succeeded.")

unstable()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def limit_calls(seconds):
    def decorator(func):
        last_called = [0]

        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called[0] < seconds:
                wait_time = round(seconds - (current_time - last_called[0]), 2)
                print(f"Too soon! Wait {wait_time} more seconds.")
                return
            last_called[0] = current_time
            return func(*args, **kwargs)

        return wrapper
    return decorator

@limit_calls(3)
def greet():
    print("Hello, user!")

greet()
time.sleep(1)
greet()
time.sleep(3)
greet()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def type_check_decor(expected_types):
    def decorator(func):
        def wrapper(*args):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i + 1} must be {expected_type.__name__}, got {type(arg).__name__}")
            return func(*args)
        return wrapper
    return decorator

@type_check_decor((int, str))
def show_user(id, name):
    print(f"User ID: {id}, Name: {name}")

show_user(1, "Alice")
# show_user("oopsy:)", "Alice")  # Uncomment to test type error

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def cache_decor(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Returning cached result...")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@cache_decor
def slow_add(a, b):
    print(f"Calculating {a} + {b}...")
    time.sleep(1)
    return a + b

print(slow_add(3, 4))
print(slow_add(3, 4))  # This one should be cached

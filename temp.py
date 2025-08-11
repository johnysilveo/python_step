def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator
def say_hi():
    print("Hi!")

say_hi()

def try_decor(func):
    def wrapper():
        print('OPA')
        func()
        print('APO')
    return wrapper

@try_decor
def welcome():
    print(str(('WELCOME').center(70)))

welcome()

def retry_decorator(retries):
    def actual_decorator(func):
        def wrapper():
            for i in range(retries):
                try:
                    return func()
                except Exception as e:
                    print(f'Try №{i+i} failed: {e}')
            print('All tries are failed')
        return wrapper
    return actual_decorator

import random

@retry_decorator(3)
def unstable():
    if random.random() < 0.7:
        raise ValueError("Random failure occurred!")
    print("Function succeeded.")

unstable()



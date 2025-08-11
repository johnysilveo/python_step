# Define a list of numbers
# numbers = [1, 2, 3, 4, 5, 6]
# Apply filter to keep even numbers and square them with map
# result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
# Print the final list
# print(result)

# Define a welcome function
def welcome():
    nickname = 'johny'  # Set nickname
    print(str(f"WELCOME {nickname.upper()}!!!").center(70))  # Print welcome message centered
welcome()  # Call the welcome function

# Define a simple decorator
def simple_decorator(my_func):
    print(str('----------------base massage from decorator---------------').center(70))  # Print message from decorator
    def simple_wrapper():  # Define wrapper function
        my_func()  # Call the original function
        newinfo = 47  # Set additional info
        print(str(f"Added massage is decor and new info is {newinfo}!").center(70))  # Print message from decorator
    return simple_wrapper  # Return wrapper function

welcome_advanced = simple_decorator(welcome)  # Apply decorator to welcome function manually

welcome_advanced()  # Call decorated welcome function

# Apply simple_decorator using @ syntax
@simple_decorator
def sayhello():
    print(str('HELLO').center(70))  # Print centered HELLO
sayhello()  # Call decorated sayhello function

# Define version 2 of decorator
def simple_decorator_v2(my_func):
    print(str('----------------base massage from decorator V2---------------').center(70))  # Print message from decorator V2
    def simple_wrapper():  # Define wrapper function
        my_func()  # Call the original function
        newinfo = 47  # Set additional info
        print(str(f"Added massage from decor V2 and new info is {newinfo}!").center(70))  # Print message from decorator
    return simple_wrapper  # Return wrapper function

# Stack two decorators: simple_decorator and simple_decorator_v2
@simple_decorator
@simple_decorator_v2
def show_list():
    print("LIST")  # Print LIST

show_list()  # Call decorated show_list function

# Define version 3 of decorator with return
def simple_decorator_v3(my_func):
    print(str('----------------base massage from decorator V3---------------').center(70))  # Print message from decorator V3
    def simple_wrapper():  # Define wrapper function
        result = my_func()  # Call the original function and save result
        newinfo = 47  # Set additional info
        print(str(f"Added massage from decor V3 and new info is {newinfo}!").center(70))  # Print message from decorator
        return result  # Return result
    return simple_wrapper  # Return wrapper function

# Apply decorator version 3
@simple_decorator_v3
def calc():
    x = 10  # Set value x
    y = 20  # Set value y
    return x + y  # Return sum
print(calc())  # Call and print result

# Define version 4 of decorator that accepts arguments
def simple_decorator_v4(my_func):
    print(str('----------------base massage from decorator V4---------------').center(70))  # Print message from decorator V4
    def simple_wrapper(argX, argY):  # Define wrapper with 2 args
        result = my_func(argX, argY)  # Call original function
        newinfo = 47  # Set additional info
        print(str(f"Added massage from decor V4 and new info is {newinfo}!").center(70))  # Print message from decorator
        return result  # Return result
    return simple_wrapper  # Return wrapper function

# Apply decorator v4 to function with two arguments
@simple_decorator_v4
def calc_v2(x, y):
    return x + y  # Return sum
print(calc_v2(2, 2))  # Call and print result

# Define decorator version 4.1 that accepts any number of arguments
def simple_decorator_v41(my_func):
    print(str('----------------base massage from decorator V4---------------').center(70))  # Print message from decorator V4
    def simple_wrapper(*args):  # Define wrapper with variable arguments
        result = my_func(*args)  # Call original function with args
        newinfo = 47  # Set additional info
        print(str(f"Added massage from decor V4 and new info is {newinfo}!").center(70))  # Print message from decorator
        return result  # Return result
    return simple_wrapper  # Return wrapper function

# Apply decorator v4.1 to function using *args
@simple_decorator_v41
def calc_v2(*args):
    return sum(args)  # Return sum of all arguments
print(calc_v2(2, 2, 2))  # Call and print result

# Define list of prices in USD
price_usd = [100, 200, 23, 34, 56, 76, 3, 12]  # List of prices

# Define function to convert USD to UAH
def to_price_new(price_list):
    return list(map(lambda x: x * 41, price_list))  # Multiply each price by 41

# Define decorator factory to apply discount
def set_disc_decor_wrap(disc):
    def change_price_decorator(func):  # Define decorator
        def wrapper(arg_list):  # Define wrapper
            result = func(arg_list)  # Call original function
            result_with_disc = list(map(lambda x: x * (1 - 0.1), result))  # Apply 10% discount
            return result_with_disc  # Return discounted list
        return wrapper  # Return wrapper
    return change_price_decorator  # Return decorator

discount = 0.1  # Set discount value
change_price_decorator = set_disc_decor_wrap(discount)  # Create decorator with discount
price_to_hrn = change_price_decorator(to_price_new)  # Apply decorator to conversion function

print(price_to_hrn(price_usd))  # Call decorated function and print result


# Import the time module to measure execution duration
import time

# Define a decorator that measures how long a function takes to run
def timing_decor(func):
    def wrapper(*args, **kwargs):  # Define the wrapper with flexible arguments
        start_time = time.time()  # Record the current time before the function runs
        result = func(*args, **kwargs)  # Call the original function and store the result
        end_time = time.time()  # Record the current time after the function runs
        total_time = end_time - start_time  # Calculate the total time taken
        print('time running: ', total_time)  # Print the execution time
        return result  # Return the original function's result
    return wrapper  # Return the wrapper function

# Apply the timing_decor decorator to the slow_func function
@timing_decor
def slow_func():
    time.sleep(2)  # Pause execution for 2 seconds
    print('done!')  # Print done message

slow_func()  # Call the decorated function to see timing

# Define a decorator that prints the types of all arguments passed to a function
def checking(func1):
    def wrapper2(*args, **kwargs):  # Define wrapper to handle all argument types
        for i in args:  # Loop through all positional arguments
            print(type(i))  # Print the type of each positional argument
        for u in kwargs.values():  # Loop through all keyword argument values
            print(type(u))  # Print the type of each keyword argument value
        return i, u  # Return the last positional and keyword value's types
    return wrapper2  # Return the wrapper function

# Apply the checking decorator to the sample function
@checking
def sample(a, b, c=5, d="hello"): pass  # Define a function with default and keyword args

print(sample(1, 2.5, d=[1, 2, 3]))  # Call the decorated function and print result

# Define a decorator factory that adds a suffix to the function's return value
def add_suffix(suffix):
    def decorator(func):  # Inner decorator function
        def wrapper(*args, **kwargs):  # Wrapper to intercept the function call
            result = func(*args, **kwargs)  # Call the original function
            return str(result) + " " + suffix  # Append the suffix to the result
        return wrapper  # Return the wrapper function
    return decorator  # Return the decorator function

# Apply the add_suffix decorator with "Mr" to get_name1
@add_suffix("Mr")
def get_name1():
    return "John"  # Return a name

# Apply the add_suffix decorator with "Ms" to get_name2
@add_suffix("Ms")
def get_name2():
    return "Jane"  # Return a name

print(get_name1())  # Print result with "Mr" suffix
print(get_name2())  # Print result with "Ms" suffix

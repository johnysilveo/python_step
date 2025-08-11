# ==== Task: Classwork with full row-by-row comments ====

# Function that greets a user with a nickname
def welcome():
    nickname = 'john'  # Set nickname variable (could be from input, but hardcoded here)
    print(str(f"WELCOME {nickname.upper()}!!!").center(70))  # Print uppercase welcome centered

welcome()  # Call the function to display greeting

print(str(type(welcome)).center(70))  # Print the type of 'welcome' (will be <class 'function'>), centered

number = 100  # Declare a global variable (not used further in this snippet)

# List of user names with different roles (admin, student, regular)
customers = ['adminKate', 'adminDjon', 'studentBill', 'studentAlice', 'Ilon']

# Function to greet user based on role in name
def welcome_user(customer):
    if customer.find('admin') != -1:  # If 'admin' is found in the string
        print(str(f"hello admin {customer}").center(70))
    elif customer.find('student') != -1:  # If 'student' is found
        print(str(f"hello student {customer}").center(70))
    else:  # Otherwise, general user greeting
        print(str(f"hello dear {customer}").center(70))

# Function to iterate over a list and apply welcome_user function to each
def hello(customerList, welcome_user):
    for customer in customerList:  # Loop through the customer list
        welcome_user(customer.lower())  # Convert each name to lowercase before greeting

hello(customers, welcome_user)  # Call function with list and function as argument

# ==== MATH FUNCTIONS (OPERATIONS) ====

def sum_ofnums(a, b):  # Function for addition
    return a + b

def multiply(a, b):  # Function for multiplication
    return a * b

def minus(a, b):  # Function for subtraction
    return a - b

# Choose which math function to return based on string input
def userChoice(c):
    print(str("Optins").center(70))  # Display operation menu centered
    print(str("1 - Sum").center(70))
    print(str("2- Multi").center(70))
    print(str("3 - minus").center(70))
    if c == '1':
        return sum_ofnums
    elif c == '2':
        return multiply
    elif c == '3':
        return minus

x = 2  # First number for operation

y = 3  # Second number for operation

# NOTE: Loop is commented out — you can uncomment it to use input and run 3 operations
# for i in range(3):
#     userAnc = input("Your choice - ")
#     print(type(userChoice(userAnc)))
#     mycalc = userChoice(userAnc)
#     print(str(mycalc(x, y)).center(70))

# ==== TASK 6 - PRODUCT OF ARBITRARY NUMBERS ====
def task6_v2(*args):  # Use *args to accept any number of values (as a tuple)
    product = 1  # Initialize product
    for i in args:  # Loop through the arguments
        product *= i  # Multiply each to the running product
    return str(product).center(70)  # Return result centered as string

# ==== FACTORIAL (RECURSION) ====
def facal(num1):
    print(str(num1).center(70))  # Print the input number centered
    if num1 == 0:
        return 1  # Factorial of 0 is 1
    else:
        return num1 * facal(num1 - 1)  # Recursive call

print(str(facal(8)).center(70))  # Print factorial of 8 centered
print(task6_v2(10,9,8,7,6,5,4,3,2,1))  # Call product function with multiple arguments

# ==== TASK 7 - MINIMUM WITH *ARGS AND RECURSION ====
def task7(*args):  # Accept variable-length tuple
    if len(args) > 1:
        return min(task7(*args[:-1]), args[-1])  # Recursively find minimum
    else:
        return args[0]  # Return final minimum

nums = [1,2,3,4,5,6,7,8,9,7,5,4,4,565,4345,6,888,-1]  # List to test with
print(str(f"min = {task7(*nums)}").center(70))  # Unpack list and call min function

# ==== FIND MAX USING BUILT-IN ====
def find_max(nums):  # Max using Python's built-in function
    return str(f"Max value is: {max(nums)}").center(70)

print(find_max([1, 2, 3, 4, 5, 6, 7, 8]))  # Call and print max from list

# ==== FIND MAX USING RECURSION ====
def find_maxR(nums):
    if len(nums) < 1:
        return max(task7(nums[:-1]), nums[-1])  # This line likely has a bug
    else:
        return nums[0]  # Return first element (base case)

print(str(f"min = {find_maxR(nums)}").center(70))  # Output result

# ==== SUM ALL NUMBERS IN LIST ====
def find_sum(nums):
    return str(f"The sum of numbers: {sum(nums)}").center(70)

def find_sumR(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + find_sumR(nums[1:])

print(find_sumR([1, 2, 3, 4, 5, 6, 7, 8]))  # Call and print total sum

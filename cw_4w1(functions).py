# A string variable storing a serial number
serial = str("T12326")  # Just storing a string in a variable

# -----------------------------
# Function to count the number of characters in a given string
def count_symbols(str11):
    print(len(str11))  # Prints the length of the string

# -----------------------------
# A simple test function
def test():
    print("Works")  # Just prints a fixed message

# -----------------------------
# Function that replaces a word in a given text with another word
def word_replacement():
    text = input("Enter your text: ")  # Get original text
    search_word = input("Enter the word to search for: ")  # Word to be replaced
    replace_word = input("Enter the replacement word: ")  # Replacement word
    new_text = text.replace(search_word, replace_word)  # Perform replacement
    print("Updated string:", new_text)  # Show result

# -----------------------------
# Function that simply prints the argument passed to it
def test1(info):
    print(info)

# Call test1 function with a string argument
test1("test1")

# -----------------------------
# Function that asks user for nickname and prints it in uppercase
def welcome():
    nickname = input(str(f"\n\tPlease enter your nickname: "))
    print(f"\n\t\t\tWELCOME {nickname.upper()}!!!")

# -----------------------------
# Function that prints 3 given numbers
def sumNums(num1, num2, num3):
    print(num1, num2, num3)

# Call sumNums with three numbers
sumNums(5, 567, 765)

# -----------------------------
# Function that returns both uppercase and lowercase versions of a name
def modifyname(user_name):
    new_name1 = user_name.upper()
    new_name2 = user_name.lower()
    return new_name1, new_name2

# Print result of calling modifyname
print(modifyname("user"))

# -----------------------------
# Basic calculator function that adds two numbers
def calc(a, b):
    return a + b  # Returns their sum

# -----------------------------
# Menu-driven calculator function
def pmmd():
    print("OPTIONS\n 1 - +\n 2 - -\n - 3 *\n - 4 /")  # Show options

    while True:
        choice = input("Enter your option: ")  # Get user choice

        # If invalid option — ask again
        if choice not in ("1", "2", '3', '4'):
            print("Wrong option, use 1 or 2 or 3 or 4")
            continue

        # Get two numbers from user
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Perform the selected operation
        if choice == "1":
            plus = num1 + num2
            print(f"Your plus is:  {plus}.")
        elif choice == "2":
            minus = num1 - num2
            print(f"Your minus is:  {minus}.")
        elif choice == "3":
            multi = num1 * num2
            print(f"Your multiplication is:  {multi}.")
        elif choice == "4":
            dev = num1 / num2
            print(f"Your division is:  {dev}.")
        break  # Exit after one operation

# -----------------------------
# Greets user differently if their login contains "admin"
def greetings(login, passw="1111"):
    if "admin" in login:
        print(f"WELCOME {login.upper()}")
        print(f"your pass {passw}")
    else:
        print(f"\n\t\t\tWELCOME {login.upper()}!!!")

# greetings(input("Enter your login: "))  # Example usage (commented)

# -----------------------------
# Function that sums all arguments (variable-length input)
def sumNum2(*args):
    print(type(args))  # Show the type (tuple)
    print(args)        # Show the full tuple
    return sum(args)   # Return the sum

# Examples (commented out)
# print(sumNum2(1, 2, 3, 4, 5, 6))
# print(sumNum2(1, 2))

# -----------------------------
# A list of users with their passwords
users = [['user1', '111'],
         ['user2', '222'],
         ['user3', '333']]

# Function to print user login and password
def printcl(*clients):  # Accepts variable number of arguments
    for i in range(len(clients)):
        if i == 0:
            print(f"Login: {clients[i]}")
        elif i == 1:
            print(f"pass: {clients[i]}")

# Loop through user list and call printcl on each
for user in users:
    printcl(*user)  # Unpack each user list into two args

# -----------------------------
# Invalid version of function (will cause error — start/end are strings)
def twonuber():
    start = input("enter start number: ")
    end = input("enter end number: ")
    # Would error: strings used in math
    for i in range(start + 1, end):
        if i % 2 != 0:
            print(i)

# -----------------------------
# Correct version: prints all odd numbers between two given numbers
def twonumber1(start, end):
    for i in range(start + 1, end):
        if i % 2 != 0:
            print(i)

# -----------------------------
# GLOBAL and LOCAL NAMESPACE EXAMPLE

# Global variable
number = 10
globalName = 'global'

# Built-in module import
import random

# Function to show local and global scope
def func1():
    global number  # Refers to the global variable `number`
    number = 0  # Modify global `number`
    print(number)  # Print local/global number
    print(globalName)  # Access globalName (global variable)

    localNum = 0  # Local variable (not used outside)

# Call function
func1()

# Check global variable after function
print(number)

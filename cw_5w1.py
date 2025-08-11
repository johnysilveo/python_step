#LAMBDA
import functools  # Imports functools for using reduce function later

def add(x):  # Defines a regular function that adds 10 to the input
    return x + 10  # Returns the result of x + 10

numbers = [2,3,4,5,6,7,8]  # List of numbers to process

for num in numbers:  # Iterates through each number in the list
    print(add(num))  # Prints the result of the add function on each number

new_num = lambda x: x + 10  # Lambda function that adds 10 to a given number

for num in numbers:  # Iterates through each number in the list
    print(new_num(num))  # Prints the result of the lambda function

for num in numbers:  # Iterates through each number in the list
    print((lambda x: x + 10)(num))  # Defines and immediately calls a lambda that adds 10

hrntodoll = 41  # Sets exchange rate from Hryvnia to Dollar
disc = 0.15  # Sets discount rate to 15%
pricedoll = lambda x: x / hrntodoll * (1 - disc)  # Lambda to convert price with discount
print(f'Price: {pricedoll(4100)}$')  # Prints the discounted dollar price of 4100 UAH

students = [['bob',70],['jane',56],['lion',88]]  # List of student names and scores
sortedstud= sorted(students, key=lambda x: x[1])  # Sorts students by their score (index 1)
print(sortedstud)  # Prints the sorted list of students

username = lambda firstname,lastname: f"full user name is {firstname.title()} {lastname.title()}"  # Lambda that formats full name
print(username('bob','norman'))  # Calls lambda with names and prints formatted result

# unumber = input("Enter number: ")  # Takes user input (commented out)
# print(unumber)  # Prints input number (commented out)

is_even = lambda x: 'even' if x % 2 == 0 else 'not even'  # Lambda that checks if number is even
print(is_even(3))  # Prints result of even-check on number 3

multi = lambda a,b,c: a * b * c  # Lambda that multiplies three numbers
print(multi(2,3,4))  # Prints the result of multiplying 2, 3, and 4

bigest = lambda a,b:a if a > b else b  # Lambda that returns the bigger of two values
print(bigest(10,50))  # Prints the bigger of 10 and 50

studyear = [2000,2002,2003,2001,1993]  # List of student birth years
studage = list(map(lambda x: 2025 - x, studyear))  # Maps each year to age by subtracting from 2025
print(studage)  # Prints the list of calculated ages

adminpass = '111'  # Admin password set to '111'
studpass = '222'  # Student password set to '222'

# def userlogin(ulog, upass):  # (commented out) Function that checks login credentials
#     if ulog.lower() == 'admin' and upass == adminpass:  # (commented out) Verifies admin login

userlogins = ['Admin', 'ASS', 'fUcK']  # List of usernames with different cases
userloginslow = list(map(str.lower, userlogins))  # Converts all usernames to lowercase
print(userloginslow)  # Prints the list of lowercase usernames

values = ['3','3.6','78.897','-3']  # List of number strings
numbers1 = list(map(float, values))  # Converts strings to float numbers
print(numbers1)  # Prints the list of float numbers

nums1 = [10,20,30]  # First list of numbers
nums2 = [1,3,5,8]  # Second list of numbers (longer, extra element ignored)
result = map(lambda a, b: a ** b, nums1, nums2)  # Raises elements of nums1 to the power of nums2
print(list(result))  # Converts result to list and prints it

#FILTER

prices = [100,30,20,5,200,1297,23433,3333,17743,2546]  # List of product prices
expensive = list(filter(lambda x: x > 200 and x < 3334, prices))  # Filters prices within specific range
print(expensive)  # Prints the filtered prices

usernames = ['abomaraga', 'baide','moornsss']  # List of usernames
userpases = ['111','222,','333']  # List of passwords
for log, passw in zip(usernames, userpases):  # Pairs usernames with passwords using zip
    print('login ',log,'password ',passw)  # Prints login-password pairs

def musum(a,b):  # Defines a function to sum two numbers
    return a + b  # Returns the sum of two inputs

from functools import reduce # Re-imports functools (already imported at top)
result = reduce(musum,[1,2,3,4,5])  # Uses reduce to sum a list using musum
print(result)  # Prints the final sum

squared = list(map(lambda x: x ** 2, nums2))
print(squared)

lengths = list(map(len, usernames))
print(lengths)





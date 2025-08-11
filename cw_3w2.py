#creat list

students =["st1", "st2", "st3"]
print(type(students))
print(students)

marks = list((10,12,9,1))
print(marks)

templist = [1,2,3,3.14,9.7, True, 'qwerty',[10, 20,30]]
print(templist)

# list indexes

print(templist[0])
print(templist[1])
print(templist[-1])

print(len(templist))
print(templist[1:3])

# max() min()

prices = [100, 10, 34, 32,88]
print(f"max price {max(prices)} and min price is {min(prices)}.")
print(f"Sum of prices {sum(prices)}")
print(f"sort st {sorted(students)}")

print([1, 2] + [3, 4])
print([1, 2] * 2)

# list methods
for student in students:
    print(student)

# list update element
prices[0] = 33
print(prices)





#>>>>>>>>>>>>>>>>>>>>>>>TEACHERS CW<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<






# ==== Creating lists ====

# A list of student names (strings)
students = ["st5", "st1", "st3"]
print(type(students))  # Shows the type of the variable (list)
# <class 'list'>
print(students)         # Prints the list of students
# ['st5', 'st1', 'st3']

# Creating a list from a tuple using the list() constructor
marks = list((10, 12, 9, 1))
print(marks)
# [10, 12, 9, 1]

# A mixed-type list: includes integers, floats, boolean, string, and a nested list
tempList = [1, 2, 3, 3.14, 9.7, True, "qwerty", [10, 20, 30]]
print(tempList)
# [1, 2, 3, 3.14, 9.7, True, 'qwerty', [10, 20, 30]]

# ==== List indexing ====

# Accessing elements by index
print(tempList[0])    # First element
# 1
print(tempList[1])    # Second element
# 2
print(tempList[-1])   # Last element (nested list)
# [10, 20, 30]

# ==== List length ====
print(len(tempList))  # Total number of elements
# 8

# ==== List slicing ====
print(tempList[1:3])     # Elements at index 1 and 2
# [2, 3]
print(tempList[:3])      # First three elements
# [1, 2, 3]
print(tempList[1:-1])    # All except the first and last
# [2, 3, 3.14, 9.7, True, 'qwerty']
print(tempList[::-1])    # Reversed list
# [[10, 20, 30], 'qwerty', True, 9.7, 3.14, 3, 2, 1]

# ==== List functions max(), min(), sum(), sorted() ====

prices = [100, 10, 34, 32, 88]
print(f"max price {max(prices)}")  # Maximum value
# max price 100
print(f"min price {min(prices)}")  # Minimum value
# min price 10
print(f"Sum of prices {sum(prices)} $")  # Sum of all prices
# Sum of prices 264 $
print(f"sort by price: {sorted(prices)}")  # Sorted list (ascending)
# sort by price: [10, 32, 34, 88, 100]
print(f"sort st {sorted(students, reverse=True)}")  # Students sorted in reverse alphabetical order
# sort st ['st5', 'st3', 'st1']

# ==== List arithmetic ====
print([1, 2] + [3, 4])  # List concatenation
# [1, 2, 3, 4]
print([1, 2] * 2)       # List repetition
# [1, 2, 1, 2]

# ==== Iterating over a list ====
for student in students:
    print(student)
# st5
# st1
# st3

# ==== Updating list elements ====

# Change first element of 'prices'
prices[0] = 33
print(prices[0])
# 33

# Add 10 to every price
for index in range(len(prices)):
    prices[index] += 10
    print(prices[index])
# 43
# 20
# 44
# 42
# 98

# ==== Common list methods ====

myList = [1, 2, 3]
print(myList)
# [1, 2, 3]

# Append a new element to the end
myList.append(4)
print("Append new last elem", myList)
# Append new last elem [1, 2, 3, 4]

# Extend the list with another list
list2 = [5, 6]
myList.extend(list2)
print("Extend list ", myList)
# Extend list  [1, 2, 3, 4, 5, 6]

# Insert elements at specific positions
myList.insert(0, 0)    # At the beginning
myList.insert(3, 10)   # At index 3
print("Insert first ", myList)
# Insert first  [0, 1, 2, 10, 3, 4, 5, 6]

# ==== Deleting elements ====

# Remove last element
myList.pop()
# (removes 6)

# Remove element at index 3
myList.pop(3)
# (removes 10)
print("after del last", myList)
# after del last [0, 1, 2, 3, 4, 5]

# Remove specific value if it exists
if 2 in myList:
    myList.remove(2)
else:
    print("no elem")
print("remove value 0", myList)
# remove value 0 [1, 3, 4, 5]

# ==== Other list operations ====

# Find index of a specific value
print("find index of value")
# find index of value
print(myList.index(1))
# 0

# Count occurrences of a value
print("count of elem ", myList.count(5))
# count of elem  1

# Sort and reverse the list
myList.sort(reverse=True)  # Descending
myList.sort()              # Ascending
myList.reverse()           # Reverse order
print(myList)
# [5, 4, 3, 1]

# Create a copy of the list and modify the copy
newList = myList.copy()
newList[0] = 111  # Changing copy does not affect the original
print(myList)     # Original list remains unchanged
# [5, 4, 3, 1]

# ==== Task 3: Sum of positive numbers entered by the user ====

number = 0
numberList = []

print("For stop press 0")
# For stop press 0

# Input loop until user enters 0
while True:
    number = int(input("Enter your number - "))
    if number == 0:
        break
    numberList.append(number)

# Filter and sum only positive numbers
posNumber = []
for num in numberList:
    if num > 0:
        posNumber.append(num)

print(f"Sum of positive nums {sum(posNumber)}")
# e.g. if input was 1, -4, 6, 0 → Sum of positive nums 7














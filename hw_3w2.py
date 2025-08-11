

number = 0
numberList = []

print("For stop press 0")

while True:
    number = int(input("Enter your number - "))
    if number == 0:
        break
    numberList.append(number)

odd = []
even = []
for num in numberList:
    if num %2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<


number = 0
numberList = []

print("For stop press 0")

while True:
    number = int(input("Enter your number - "))
    if number == 0:
        break
    numberList.append(number)

print(f"max number {max(numberList)} and min number is {min(numberList)}.")



>>>>>>>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<<<<<<
import random
numbers = []

for i in range(3000):
    numbers.append(random.randint(-999999999, 99999999999))


print(f"Max number: {max(numbers)}")
print(f"Min number: {min(numbers)}")
print(f"This number of elements in the list: {len(numbers)}")
print(f"Number of zeroes in the list: {numbers.count(0)}")

>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<

nums = input("Enter a list of integers separated by space: ").split()
nums = [int(i) for i in nums]

limit = int(input("Enter a number: "))

filtered = [n for n in nums if n >= limit]
print("Result:", filtered)

>>>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<<<<<<<<<

strings = input("Enter a list of strings separated by space: ").split()

shortest = min(strings, key=len)
longest = max(strings, key=len)
print("The shortest string is:", shortest)
print("The shortest string is:", longest)

>>>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<<<<

str1 = input("Enter a list of words separated by space: ").split()
let = input("Enter a letter you want words to start with: ")
temp_list1 = []
for w in str1:
    if w.lower().startswith(let.lower()):
        temp_list1.append(w)
print(temp_list1)




>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 7<<<<<<<<<<<<<<<<<<<


str11 = input("Enter an operation like '+ - * /': ")

if '+' in str11:
    num1, num2 = str11.split('+')
    print(int(num1) + int(num2))
elif '-'in str11:
    num1, num2 = str11.split('-')
    print(int(num1) - int(num2))
elif '*' in str11:
    num1, num2 = str11.split('*')
    print(int(num1) * int(num2))
elif '/' in str11:
    num1, num2 = str11.split('/')
    print(int(num1) / int(num2))




#>>>>>>>>>>>>>>>>>>>>>>>>TASK 8<<<<<<<<<<<<<<<<<<<<

numberList = []
print("For stop press 0")

while True:
    number = int(input("Enter your number - "))
    if number == 0:
        break
    numberList.append(number)

non_negatives = [x for x in numberList if x >= 0]
non_negatives.sort()

#Not finished



























































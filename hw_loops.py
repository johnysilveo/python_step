# #>>>>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<
#
print("WELCOME USER")

num = int(input("Enter your number and see what will happend neeeext: "))
count = 1

while count <= 11:
    result = num * count
    print(f"{num} * {count} = {result}")
    count += 1

# #>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<
#

while True:
    print("\nChoose currency to convert from UAH:")
    print("1 - USD")
    print("2 - EUR")
    print("3 - GBP")
    print("4 - JPY")
    print("5 - Exit")

    choice = input("Enter the operation number (1–5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select 1–4 or 5 to exit.")
        continue

    amount = float(input("Enter amount in UAH: "))
    rate = float(input("Enter exchange rate (UAH per 1 unit of selected currency): "))

    converted = amount / rate

    if choice == "1":
        print(f"{amount} UAH = {converted:.2f} USD")
    elif choice == "2":
        print(f"{amount} UAH = {converted:.2f} EUR")
    elif choice == "3":
        print(f"{amount} UAH = {converted:.2f} GBP")
    elif choice == "4":
        print(f"{amount} UAH = {converted:.2f} JPY")


#>>>>>>>>>>>>>>>>TASK 4 V 1.0 <<<<<<<<<<<<<<<

print("\nEnter 5 numbers: ")
num1 = int(input("Num1"))
num2 = int(input("Num2"))
num3 = int(input("num3"))
num4 = int(input("Num4"))
num5 = int(input("Num5"))

numbers =[num1,num2,num3,num4,num5]

print(f"The maximum is : {max(numbers)}")

# #>>>>>>>>>>>>>>>>TASK 4 V 2.0 <<<<<<<<<<<<<<<

numbers =[]
print("\nEnter 5 numbers: ")

for i in range(5):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

print(f"The maximum is: {max(numbers)}")



#>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<

start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))

while True:
    number = int(input("Enter number inside the range: "))
    if start <= number <= end:
        break
    else:
        print("Number is off the range. One more time!")

for i in range(start, end + 1):
    if i == number:
        print(f"!{i}!", end=" ")
    else:
        print(i, end= " ")

#----------------SECRET NuMBER----------

import random

ran1 = random.randint(1, 500)
print("Welcome to the game of\n\t'Secret number'.")

guess = int(input("Enter your guess: "))

while guess != ran1:
    if guess < ran1:
        print("Too low")
    elif guess > ran1:
        print("Too high")

    guess = int(input("Try again: "))

print(f"You guessed it {ran1} right!\nCongratulations!!!\nYour cake is right around the corner...")




#>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<

print("\nMENU\nChoose your shape\nSquare - 1\nRectangle - 2")

while True:
    choice = input("\nEnter your choice: ")
    if choice not in ("1", "2"):
        print("Wrong option, use 1 or 2")
        continue

    if choice == '1':
        side = int(input("Enter length of the square: "))
    else:
        length = int(input("Enter length: "))
        height = int(input("Enter height: "))
    break

symbol = input("Enter symbol to fill the shape: ")

if choice == '1':
    for i in range(side):
        print(symbol * side)
else:
    for i in range(height):
        print(symbol * length)











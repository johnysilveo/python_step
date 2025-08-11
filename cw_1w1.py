#logic type of var - bool -- True or False

#test = True
#test1 = False
#print("Here is your info ",test,"and",test1,"for this vars")
#print(type(test))

#logic operators - > < ==
#speed = int(input("enter speed"))
#print("Before if")
#if speed > 25:
#    print("car speed is over 25 MPH")
#elif speed < 25:
#    print("Car's speed is under 25MPH")


#print("after if")
#if speed <10 and speed > 30:
#    print("Your speed is out of range")
#    if speed < 30 and speed > 10:
#        print("your spee is within rhe range")

#year = int(input("Enter year to know wheather it leap or not "))
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#    print(f"Year {year} is leap!")
#else:
#    print(f"Year {year} is not leap")

#user_age = int(input("Enter age: "))

#if user_age < 0 or user_age > 120:
 #   print("Wrong age")
#elif user_age < 3:
#   print("Toddler")
#elif user_age < 11:
#    print("Is baby")
#elif user_age < 20:
#    print("Teenager")
#elif user_age < 65:
#    print("Work force")
#else:
#    print("Elderly")

#number = int(input("Enter a number: "))
#if number % 2 == 0:
#    print(f"{number} is an even number.")
#else:
#    print(f"{number} is an odd number.")

#number = int(input("Enter a number: "))
     #>>>>>task 2<<<<<<
#if number % 7 == 0:
#    print("The number is divisible by 7")
#else:
#    print("The number is NOT divisible by 7")

#>>>>>>>>>>TASK 3<<<<<<<<<

#num1 = int(input("Enter num1"))
#num2 = int(input("Enter num2"))
#if num1 > num2:
#    print(f"Num2 is max {num2}")
#else:
#    print(f"Num1 is max {num2}")

#>>>>>>>>>TASK %<<<<<<<<<<<<<
# print("Choose an operation:")
# print("1 — Sum")
# print("2 — Difference")
# print("3 — Product")
# print("4 — Average")
#
# choice = input("Enter the operation number (1-4): ")
#
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
#
# if choice == "1":
#     print("Sum:", a + b)
# elif choice == "2":
#     print("Difference:", a - b)
# elif choice == "3":
#     print("Product:", a * b)
# elif choice == "4":
#     print("Average:", (a + b) / 2)
# else:
#     print("Invalid choice!")

#>>>>>>>>>>>TASK 6<<<<<<<<<<<<<
print("Choose currency")
print("USD -1")
print("EUR -2")
print("GBP - 3")
print("JPY - 4")

choice = input("Enter the operation number to convert UAH (1-4): ")
amount = float(input("Enter amount "))
rate = float(input("Enter exchange rate "))
if choice == "1":
    converted = amount / rate
    print(f"UAH = {converted}","USD")
elif choice =="2":
    eur = amount * rate
    print(f"Uah tom USD is {eur} ")
elif choice == "3":
    gbp = amount / rate
    print(f"{amount} UAH is equal to {gbp} UAH")
elif choice =="4":
    jpy = amount / rate
    print(f"{amount:2f} UAH is equal to {jpy} JPY")
else:
    print("somthing wrong")


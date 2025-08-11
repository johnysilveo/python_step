#>>>>>>>>>>>>>TASK !<<<<<<<<<<<<<<<
while True:
    enter_sec = int(input("Enter amount of seconds passed since the beginning of the day: "))

    day_sec = 60 * 60 * 24

    if 0<= enter_sec <= day_sec:
        break
    else:
        print("Invalid number, please try again!")

left = day_sec - enter_sec

hours = left // 3600
minutes = (left % 3600) // 60
seconds = left % 60

print(f"Till the en dof the day {hours} hours {minutes} minutes and {seconds} seconds.")


#>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<

print("WELCOME")
print("OPTIONS\n 1 - area\n 2 - perimeter")

while True:
    choice = input("Enter your option: ")

    if choice not in ("1", "2"):
        print("Wrong option, use 1 or 2")
        continue

    rad = int(input("Enter radius of your circle: "))

    if choice == "1":
        area = 3.14 * rad ** 2
        print(f"Area of the circle is {area}.")
    elif choice == "2":
        perimeter = 2 * 3.14 * rad
        print(f"Perimeter of the circle is {perimeter}.")
    break

#>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<

price = int(input("Enter price of the item: "))
count = int( input("Enter count: "))
percent = int(input("Enter your discount: % "))

total = price * count
disc =  total * percent / 100
result = total - disc
print(f"Price is {total}.\nDiscounted price is {result}\nPlease pay at the register{result}.\nYour savings today is {disc}.\nHave a good day.\nThank you for your business!\nPlease come again soon!")


#>>>>>>>>>>>>>>>>>>>TASK 4 <<<<<<<<<<<<<<<<<<<<

size = int(input("enter size of your file using GB: "))
speed = int(input("Enter your internet connection speed BPS: "))

seconds = int((size * 8_000_000_000) / speed)
minutes = int(seconds / 60)
hours = int(minutes / 60)
days = int(hours / 24)
week = int(days / 7)
print(f"Your file will be downloaded in {week} weeks or {days} days or {hours} hours or {minutes} minutes or {seconds} seconds")



#>>>>>>>>>>>>>>>>>>>>>>TASK 5 <<<<<<<<<<<<<<<<<<<<
while True:
    hours = int(input("Enter your hours in format 0-23: "))

    night = [0,1,2,3,4,5,6]
    morning = [7,8,9,10,11,12]
    day = [13,14,15,16]
    evening = [17,18,19,20,21,22,23]
    allday = night + morning + day + evening

    if hours in night:
        print("Good night")
        break
    elif hours in morning:
        print("Good morning")
        break
    elif hours in day:
        print("Good day")
        break
    elif hours in evening:
        print("Good evening")
        break
    else:
        print("Invalid input! Try again with a number from 0 to 23.")

#>>>>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<<<<<<

while True:
    temp = int(input("Enter temperature in Celsius: "))

    if temp <= -10:
        print("It is verrrrrry cold!")
        break
    elif -9 <= temp < 0:
        print("It is freezing")
        break
    elif 0 <= temp < 15:
        print("It is cold")
        break
    elif 15 <= temp <= 25:
        print("It is warm")
        break
    elif temp > 25:
        print("It is hot")
        break
    else:
        print("Invalid input! Try again.")












            # FIRST TASK
meters = float(input("Enter amount of meters: "))
sm = meters * 100
dm = meters * 10
mm = meters * 1000
miles = meters / 1609.34
print("Cantimeters: ",sm)
print("Decimeters: ",dm)
print("Milimeters: ",mm)
print("Miles: ",miles)
            #SECOND TASK
#diag1 = float(input("Entaer diagonal1: "))
#diag2 = float(input("Enterdiagonal 2: "))
#surfarea = (diag1 * diag2) / 2
#print("Diamond surface area is equal to: ", surfarea)
            #THIRD TASK
#msall = float(input("Enter monthly sallery: "))
#cardpay = float(input("Enter monthly card payment: "))
#util = float(input("Enter monthly utilitys: "))
#res = msall - cardpay - util
#print("Here what will be left for you: ", res)
            #Forth Task
#print("\t\t\tWelcome to road trip planning calculator")
#miles = float(input("Enter how long is your trip Sir: "))
#mpg = float(input("Enter your MPG Sir: "))
#price = float(input("Enter expected gas price Sir: "))
#res = (miles / mpg) * price
#print("Here how much gas will cost:", res, "on this trip. Have a wonderful trip, Sir!")
            #Fifth task
#a = int(input("Enter: "))
#b = int(input("Enter: "))
#c = int(input("ENter: "))
#print("Here:", str(a) + str(b) + str(c))
            #Sixth task
#num = input("Enter 4-digit number")
#res = 1
#for digit in num:
#    res *= int(digit)
#print("Here is result: ",res)
            #Seventh task
price = float(input("Enter price of the car per day: "))
days = float(input("Enter how many days you will have the car: "))
dep  = float(input("Enter deposit amount: "))
dueto = price * days
taxrate = 7.88
tax = dueto * (taxrate / 100)
totalbeforedeposit = dueto + tax
totalduetoday = totalbeforedeposit - dep
costperday = totalbeforedeposit / days
print("\n---- BILL SUMMARY ----")
print(f"Base (without tax): ${dueto:.2f}")
print(f"Tax (7.88%):        ${tax:.2f}")
print(f"Total before deposit: ${totalbeforedeposit:.2f}")
print(f"Deposit subtracted:  -${dep:.2f}")
print(f"Amount to pay today:  ${totalduetoday:.2f}")
print(f"Final cost per day (w/ tax): ${costperday:.2f}")





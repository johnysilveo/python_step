# there is 2 cycles for and while
#there is function atributes as "end"
#
# count = 1
# while count < 10:
#     print(f"count = ", count)
#     count += 1
# num = 0
# while num != 10:
#     num = int(input("enter num: "))
#     print(num)
#     if num == 0 or num == 100:
#         print("stop loop")
#         break
# print("end while)")

# for i in 1, 2, 3,4,5:
#     print(i)
# for s in "python and just some other stuff like whatever i mean you know just letterly nothing to see here just move one stop looking comon leave":
#     print(s,end=" _ ")


    #function "range()"
# print(">>>>>>>>>>>>RANGE<<<<<<<<<<<<<")
# for num in range(1, 11, 2):
#         print(num)
# print(">>>>>>>>>>END OF RANGE<<<<<<<<<<")

         # break

#_______FOR WITH CONYINUR_____________
# for num in range(100):
#         if num % 10 == 0:
#                 print(num)
#         else:
#                 continue #or pass as a simple plug
#         print("END body")
#
                # ERROORRR
# floor = int(input("enter floor "))
# energy = 17
# print(f"i  on the {floor} floor")
#
# while floor != 5:
#         step = 0
#         if floor == 3:
#                 print("i will take an elevator")
#                 break
#                 while step != 20:
#                         step += 1
#                         if energy == 0:
#                                 print("i'm tired!")
#                                 floor += 1
#                                 print(f"Good im on the {floor} floor")
#                                 print("im at home!")


       #>>>>>>>>>>>>CORRRRRECT<<<<<<<<<<<

# floor = int(input("Enter floor: "))
# energy = 17
# print(f"I am on the {floor} floor")
#
# while floor != 5:
#     if floor == 3:
#         print("I will take an elevator")
#         break
#
#     step = 0
#     while step != 20:
#         step += 1
#         energy -= 1  # Decrease energy on each step
#         if energy == 0:
#             print("I'm tired!")
#             break
#
#     floor += 1
#     print(f"Good, I'm on the {floor} floor")
#
# if floor == 5:
#     print("I'm at home!")

# num1 =int(input("Enter"))
# num2 =int(input("Enter"))
# for num in range (num1, num2,-1):
#         if num % 2==0:
#                 print(num)

# num1 =int(input("Enter"))
# num2 =int(input("Enter"))
# dir = input("1")
# if dir == '1':
#
# for num in range (num1, num2 + 1):
#         if num % 2!=0:
#                 print(num)
#         elif dir == '2':
#                 for num in range(num2, num1, + 1, -1):
#


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# if a > b:
#         temp = a
#         a = b
#         b = temp
# else:
#         pass
# for num in range(a ,b+1, -1):
#         if num % 2 != 0:
#                 print(num)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# if a > b:
#     start = a
#     end = b
#     step = -1
# else:
#     start = a
#     end = b
#     step = 1
#
# for num in range(start, end + step, step):
#     if num % 2 != 0:
#         print(num)



# a = int(input("Enter first number: "))
# count =1
# fac = 1
# while count <= a:
#         fac *= count
#         count += 1
#         print(f"Factorial of {a} is {fac}.")

a = int(input("enter num "))
b = int(input("enter "))
if a > b:
        temp = a
        a = b
        b = temp

sum_nums = 0
count = 0
for in range(a, b + 1):
        sum_nums += i
        count += 1
def welcome():
    nickname = 'evgeniy'
    print(str(f"WELCOME {nickname.upper()}!!!").center(70))
welcome()



def gcdRec(a,b):
    if b == 0:
        return a
    if a < b:
        return gcdRec(b,a)
    else:
        return gcdRec(b,a%b)


print(gcdRec(9,99))

def sum_in_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_in_range(a + 1, b)

print(sum_in_range(1,5))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VERSION 1<<<<<<<<<<<<<<<<<<<<<<<<<
def print_star():
    promt = "Please enter number of stars to be printed: "
    padding = (70 -len(promt)) // 2
    number = input(" " * padding + promt)
    print(f'*' * int(number))
print_star()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VERSION 2<<<<<<<<<<<<<<<<<<<<<<<<<
def print_star1(count):
    if count == 0:
        return
    else:
        print('*', end='')
        print_star1(count -1)
print_star1(9)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<<<<<<<<<

import random

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VERSION 3<<<<<<<<<<<<<<<<<<<<<<<<<
def some():
    numbers = [random.randint(1,99) for i in range(100)]
    last = numbers[0:10]
    last_sum = sum(last)
    return last_sum

print(f"\n\t\t\tHere is the result: {some()}")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VERSION 2<<<<<<<<<<<<<<<<<<<<<<<<<
def some2():
    some1 = random.randint(0,100)
    if some1 == 0:
        return []
    numbers = list(range(some1))
    last = numbers[0:10]
    last_sum = sum(last)
    return last_sum

print(f"\n\t\t\tHere is the result: {some2()}")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VERSION 1<<<<<<<<<<<<<<<<<<<<<<<<<
def some():
    some1 = random.randint(1,100)
    if some1 == 0:
        return
    numbers = list(range(some1))
    last = numbers[-10:]

    for i in last:
        return i
print(f"here is the result {some()}")

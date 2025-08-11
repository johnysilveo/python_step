def welcome():
    nickname = 'john'#input(f"\n\t\t\t\t\t   Please enter your nickname: ")
    print(str(f"WELCOME {nickname.upper()}!!!").center(70))

welcome()
print(str(type(welcome)).center(70))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<<<<<<<<<<
def twonumber1(start, end):
    if start > end:
        start, end = end, start
    for i in range(start + 1, end):
        if i % 2 != 0:
            print(i)

twonumber1(9, 1)
#>>>>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<
def returnmin(*args):
        print(f"\n\tThe smallest number is {min(args)} out of {len(args)}.\n\t\t\t\tThank YOU!")


returnmin(1,2,3,4,5,6,7,8,9,76554,5432,234,67,543,3456,-1,-3456)
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<<<<<<<
def task3(start, end):
    if start > end:
        start, end = end, start

    product = 1
    for i in range(start, end + 1):
        product *= i
        print("task3 ", product)
    return product

task3(9, 2)
#>>>>>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<<<
def task4(num1):
    print("Task4".center(70))
    print(f"The length is of your number is: {len(str(num1))}".center(70))

task4(2345678)
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<<<<<<<<<

def task5(num1):
    num1_str = str(num1)
    if num1_str == num1_str[::-1]:
        return str(f"It is a palindrome {num1}").center(70)
    else:
        return "Not a palindrome".center(70)
print(task5('madam'))
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<<<<<
def task6(numbers):
    product = 1
    for i in numbers:
        product *= i
    return str(product).center(70)

print(task6([1,2,3,4,5,6,7,8,9]))
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 6v2 <<<<<<<<<<<<<<<<<<<<<<<<<

def task6_v2(*args):
    product = 1
    for i in args:
        product *= i
    return str(product).center(70)

print(task6_v2(1,2,3,4,5,6,7,8,9))
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 7<<<<<<<<<<<<<<<<<<<<<<<<<
def task7(*args):
    return str(min(args)).center(70)

print(task7(1,2,3,4,5,6,7,8,9,7,5,4,4,565,4345,6,888,-1))
#>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 8<<<<<<<<<<<<<<<<<<<<<<<<<
def prime_or_not(num1):
    for i in num1:
        temp = 1
        if i / 1 and i / i:
            print(str(f"Here is a list of prime numbers: {i}").center(70))
        else:
            print(str(f"not").center(70))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 9<<<<<<<<<<<<<<<<<<<<<<<
def find_one(*args):
    prompt = "Please enter your value to search for: "
    padding = (70 - len(prompt)) // 2
    raw_target = input(" " * padding + prompt)

    if raw_target.isdigit():
        target = int(raw_target)
    elif '.' in raw_target and raw_target.replace('.', '', 1).isdigit():
        target = float(raw_target)
    else:
        target = raw_target

    count = args.count(target)
    print(str(f"There are {count} occurrence(s) of {target} in the list").center(70))

    return ''
print(find_one(1,2,3,4,5,6,7,7,7,7,8,8,8,9,9,9,99,8,7,6,))






















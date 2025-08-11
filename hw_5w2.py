numbers = [-1,1,2,3,4,5,6,9.5]
numbers1 = [6,5,4,3,2,1,-1]
strings = ['rdfr frfrgrfef rrrfdcrrv r','recscddcxwdc ecddrvc dcvrvrfvdce vcdvcd']
fruit = ["Apple", "banana", "cherry",'Apricot']
logins = ['alice', 'bob', 'charlie']

#>>>>>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<<<<<<<<<<<<
result = list(map(lambda x: x ** 2, numbers))
print(result)

for i in list(map(lambda x: x ** 2, numbers)):
    print(i)
#>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<<<<

length = list(map(len , strings))
print(length)

def length1(str1):
    return list(map(len, str1))
print(length1(strings))
#>>>>>>>>>>>>>>>>>>>>>TASK3<<<<<<<<<<<<<<<<<<<<<<<<
def is_even(a):
    return a % 2 == 0
print(list(filter(is_even, numbers)))

for u in list(filter(lambda x: x % 2 == 0, numbers)):
    print(u)

#>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<<

def starts_with(s):
    return s.lower().startswith('a')
print(list(filter(starts_with, fruit)))

#>>>>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<<<<<<<<

def divi3(d):
    return d % 3 == 0
def to_str(x):
    return f"{x} is divisible by 3"
res = list(map(to_str, filter(divi3, numbers)))
print(list(filter(divi3, numbers)))
print(res)

#>>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<<<<

print(list(zip(numbers, numbers1)))

#>>>>>>>>>>>>>>>>>>>>>TASK 7<<<<<<<<<<<<<<<<<<<<<<<<

ziped = list(zip(numbers, numbers1))

def multi(f,g):
    return f * g
for y in (list(map(multi, numbers, numbers1))):
    print(y)

def multi1(f_g):
    return f_g[0] * f_g[1]
for y in map(multi1, ziped):
    print(y)

#>>>>>>>>>>>>>>>>>>>>>TASK 8<<<<<<<<<<<<<<<<<<<<<<<<

def or_or(a_s):
    return a_s[0] > a_s[1]
print(list(filter(or_or, ziped)))
print(list(filter(lambda p: p[0] > p[1], ziped)))


#>>>>>>>>>>>>>>>>>>>>>TASK 9<<<<<<<<<<<<<<<<<<<<<<<<

def is_positive(q):
    return q >= 0
print(list(filter(is_positive, numbers)))
print(list(filter(lambda q: q >= 0, numbers)))

#>>>>>>>>>>>>>>>>>>>>>TASK 10<<<<<<<<<<<<<<<<<<<<<<<<

# lower = int(input("Enter lower limit: "))
# upper = int(input("Enter upper limit: "))

# def in_range(x):
#     return lower <= x <= upper
#
# filtered = list(filter(in_range, numbers))
# print(filtered)

#>>>>>>>>>>>>>>>>>>>>>TASK 11<<<<<<<<<<<<<<<<<<<<<<<<

def is_int(x):
    return isinstance(x,int)
ints = list(filter(is_int, numbers))
print(ints)

#>>>>>>>>>>>>>>>>>>>>>TASK 12<<<<<<<<<<<<<<<<<<<<<<<<

print(list(map(lambda x: '$' + x, logins)))


#>>>>>>>>>>>>>>>>>>>>>TASK 13<<<<<<<<<<<<<<<<<<<<<<<<

ziped_list = list(zip(numbers, fruit,logins))
print(ziped_list)

#>>>>>>>>>>>>>>>>>>>>>TASK 14<<<<<<<<<<<<<<<<<<<<<<<<

print(list(map(str, numbers)))  # in compare to loops we used before, this is way batter!!!!

str_numbers = []
for num in numbers:
    str_numbers.append(str(num))
print(str_numbers)

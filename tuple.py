# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які
# унікальні для кожного списку.
#
d = (1,2,13,456,6789)
a = (1,2,3,6,4,8,0,1,2,3,6,4)
b = (1,2,3,4,6,8,9,8,3,4,6,8,9,8)
c = (1,2,4,6,5,8,3,1,2,4,6,5,8,3)
only_a = set(a) - set(b) -set(c)
only_b = set(b) - set(a) - set(c)
only_c = set(c) - set(a) -set(b)
print(f"Task 1\nUnic in set (a): {only_a}\nUnic in (b): {only_b}\nunic in (c): {only_c}")
# Завдання 2


for i, (x, y, z) in enumerate(zip(a, b, c)):
    if x == y == z:
        print(f"Task 2\nSame at index {i}: {x}")

# Завдання 3

#
print("TASK 3")
for q in d:
    digits = len(str(abs(q)))
    print(f"{q} has {digits} digits")


# Завдання 4


students = [("Ганна", 22), ("Іван", 16), ("Марія", 20), ("Петро", 25)]
for name, age in students:
    if age >= 18:
        print(f"{name} is {age} years old.")

# Завдання 5


merch = [('Яблука', 10), ('Молоко', 5), ('Хліб', 3), ('Масло', 2)]
total = sum(count for product, count in merch)
print(f"Загальна кількість товарів: {total}")



# Завдання 6


authors = [('Майстер і Маргарита', 'Михайло Булkаков', 1967), ('Злочин і покарання',
'Федор Достоєвський', 1866),('Війна і мир', 'Лев Толстой', 1869), ('1984', 'Джордж Оруелл', 1949)]
unic_auth = set()
for _, author, _ in authors:
    unic_auth.add(author)
    print("Список авторів без повторень:")
    for author in unic_auth:
        print(author)


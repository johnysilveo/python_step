# import sys
# sys.path.append('D:/Py')
# print('method 1')
#
# with open("D:/Py/snakeh.py") as f:
#     exec(f.read())
# print('method2')

# try:
#     print('we r opening a file...')
#     file = open('text.txt','r', encoding='utf-8')
#     # file.write(f"Метод файлового обєкта close() автоматично закриває файл, \nпри цьому втрачається будь-яка незбережена інформація. Працювати з файлом (читати, записувати) після цього не можна. \nPython автоматично закриває файл, якщо файловий об'єкт до якому він прив'язаний присвоюється іншому файлу. \nОднак, гарною практикою є явне закриття файлу командою")
#     # data1 = file.read(10)
#     # print('!!!!!!',data1)
#     # data2 = file.read(10)
#     # print('!!!!!',data2)
#     # data3 = file.readline()
#     # print(data3)
#     # alllines = file.readlines()
#     # print(alllines)
#     # for line in file:
#     #     print(line)
#     lines = ()
#     file.seek(150)
#     print(file.tell())
#     print(file.read(500))
#     file.close()
# except Exception as ex:
#     print('we r can',"'",'t open a file',ex)

# with open("text.txt") as file1,open('try.txt','r') as file2:
#     file2.write(file1.read().lower())


# def text_replacement(file_name, old_text, new_text):
#     with open(file_name,'r+') as file:
#         data = file.read()
#         data.replace(old_text, new_text)
#         file.write(data)
#         file.close()
#
# def read_from_file(file_name):
#     with open(file_name) as file:
#         data = file.read()
#         print(data)
#         return data

# Напишіть програму, яка створює текстовий файл output.txt і записує в нього рядок "Hello, world!".
# # Завдання 2
# # Напишіть програму, яка відкриває файл output.txt, читає його вміст і виводить у консоль.
# Завдання 3
# Напишіть програму, яка копіює вміст файлу data.txt у новий файл backup.txt.
# Завдання 4
# Напишіть програму, яка підраховує кількість рядків у файлі data.txt і виводить результат.
# try:
    print('we r opening a file...')
    file = open('output.txt','r', encoding='utf-8')
    # file.write("\nHello World")
    for line in file:
        print(line)
except Exception as ex:
    print('we r can',"'",'t open a file',ex)

try:
    with open('output.txt', 'r', encoding='utf-8') as source:
        data = source.read()

    with open('backup.txt', 'w', encoding='utf-8') as backup:
        backup.write(data)
    print("File copied.")
except Exception as ex:
    print("an error has occurred in the process:", ex)


try:
    with open('backup.txt', 'r', encoding='utf-8') as file:
        line_count = sum(1 for _ in file)
    print("count of rows:", line_count)
except Exception as ex:
    print("error read:", ex)

# Завдання 5
# Напишіть програму, яка відкриває файл data.txt, аналізує його вміст і
# створює звіт summary.txt,
# у якому вказується кількість рядків, слів і символів у файлі.

try:
    with open('backup.txt', 'r', encoding='utf-8') as source:
        data = source.read()

        line_count = len(data.splitlines())
        leters = len(data)
        words = len(data.split())
        report = (
            f"rows = {line_count}\n"
            f"leters = {leters}\n"
            f"words = {words}\n"
        )
    with open('summary.txt', 'a', encoding='utf-8') as backup:
        backup.write(report)
        print('ur summary is ready')
except Exception as ex:
    print("an error has occurred in the process:", ex)

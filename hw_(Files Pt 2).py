import pickle
from itertools import zip_longest




# text_py = "Python is fucking widely fuck known for its pussy flexibility, especially when compared to bullshit Java. Python’s simple syntax and dynamic typing allow for faster development and easier debugging and what not. Unlike fucking Java, which is verbose and strictly object-oriented, Python supports multiple paradigms, including procedural and functional programming. This makes Python more adaptable for different tasks like scripting, automation, or AI. Python’s vast library ecosystem also speeds up development. While Java is better for large, structured systems, Python offers quick solutions and rapid prototyping. Developers often choose Python for its readability and ease of use. In short, Python provides flexibility where Java can feel rigid."
# with open('python.txt','wb') as file:
#      pickle.dump(text_py,file)
# words = "fucking, bullshit, fuck, pussy"
# with open('words.txt','wb') as file:
#      pickle.dump(words,file)

def change_py(word1,word2):
    with open('python.txt','rb') as file:
        content = pickle.load(file)
        edited = content.lower().replace(word1,word2)
        with open('python.txt','wb') as file:
            pickle.dump(edited,file)
change_py('python','java')


def count_chars_in_lines():
    with open('data.txt', 'rb') as file:
        content = pickle.load(file)
        lines = content.splitlines()

        result = []
        for i, line in enumerate(lines, 1):
            result.append(f"Line {i}: {len(line)} characters")

    with open('char_count.txt', 'wb') as pedofile:
        pickle.dump(result, pedofile)



def compare(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data1 = pickle.load(f1)
        data2 = pickle.load(f2)

    lines1 = set(data1.splitlines())
    lines2 = set(data2.splitlines())

    only_in_file1 = lines1 - lines2
    only_in_file2 = lines2 - lines1

    result = []
    result.append(f"Lines in {file1} but not in {file2}:")
    result.extend(only_in_file1)
    result.append(f"\nLines in {file2} but not in {file1}:")
    result.extend(only_in_file2)

    with open(output_file, 'wb') as out:
        pickle.dump('\n'.join(result), out)

# compare('text11.txt','text22.txt','report.txt')

def censor(file1,file2,out_put_file):

    # Text to be censored

    with open(file1,'rb') as file:
        content_s_raw = pickle.load(file)
        content_s = [word.strip().lower() for word in content_s_raw.split()]
        print(f"\n\t\t\t{content_s}")
        print(f"\n\t\t\t{content_s_raw}")

        # Bad words

    with open(file2,'rb') as file:
        content_w_raw = pickle.load(file)
        content_w = [word.strip().lower() for word in content_w_raw.split(',')]
        print(f"\n\t\t\t{content_w}")
        print(f"\n\t\t\t{content_w_raw}")

    # Replacement

    text = content_s_raw.lower()
    for word in content_w:
        text = text.replace(word, '***')

    # save

    with open(out_put_file,'wb') as file:
        pickle.dump(text, file)

# censor('python.txt','words.txt','report.txt')


# Online store menu>>>

import pickle

def orders_menu():
    try:
        with open('orders.txt', 'rb') as file:
            orders = pickle.load(file)
    except:
        orders = {}

    while True:
        print('\n1. Add Order\n2. Show Orders\n3. Find by Number\n4. Update Order\n5. Delete Order\n6. Exit')
        choice = input('>>> ')

        if choice == '1':
            number = input('Order number: ')
            item = input('Item name: ')
            quantity = input('Quantity: ')
            price = input('Price: ')
            orders[number] = [item, quantity, price]

        elif choice == '2':
            for k, v in orders.items():
                print(k, v)

        elif choice == '3':
            number = input('Order number to find: ')
            if number in orders:
                print(orders[number])
            else:
                print('Not found')

        elif choice == '4':
            number = input('Order number to update: ')
            if number in orders:
                quantity = input('New quantity: ')
                price = input('New price: ')
                orders[number][1] = quantity
                orders[number][2] = price
            else:
                print('Not found')

        elif choice == '5':
            number = input('Order number to delete: ')
            if number in orders:
                del orders[number]
            else:
                print('Not found')

        elif choice == '6':
            with open('orders.txt', 'wb') as file:
                pickle.dump(orders, file)
            break

# Students

def students_menu():
    try:
        with open('students.txt', 'rb') as file:
            students = pickle.load(file)
    except:
        students = {}

    while True:
        print('\n1. Add Student\n2. Show All\n3. Find by Name\n4. Update\n5. Delete\n6. Exit')
        choice = input('>>> ')

        if choice == '1':
            name = input('Name: ')
            course = input('Course: ')
            avg = input('Average grade: ')
            students[name] = [course, avg]

        elif choice == '2':
            for k, v in students.items():
                print(k, v)

        elif choice == '3':
            name = input('Student name: ')
            if name in students:
                print(students[name])
            else:
                print('Not found')

        elif choice == '4':
            name = input('Student to update: ')
            if name in students:
                course = input('New course: ')
                avg = input('New average: ')
                students[name] = [course, avg]
            else:
                print('Not found')

        elif choice == '5':
            name = input('Student to delete: ')
            if name in students:
                del students[name]
            else:
                print('Not found')

        elif choice == '6':
            with open('students.txt', 'wb') as file:
                pickle.dump(students, file)
            break



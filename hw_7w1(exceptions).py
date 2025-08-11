#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def name_age():
    while True:
        try:
            name = input("enter ur name: ")
            if not name.isalpha():
                raise ValueError ("Name must containe characters only")
            age = input("enter ur age: ")
            if not age.isdigit():
                raise ValueError("age must contain only digits.")
            age = int(age)
            if age <= 0 or age >= 130:
                raise ValueError ("age must be between 0 and 130.")
            print(f"Name is: {name}\nAge is: {age}")
            with open('Names.txt', 'a', encoding='utf-8') as new_file:
                report = f"Name is {name}\nAge is {age}\n"
                new_file.write(report)
            break
        except ValueError as ve:
            print(ve)
# name_age()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def name_age_v2(name, age):
    while True:
        try:
            if not name.isalpha():
                raise ValueError ("Name must containe characters only")
            if not age.isdigit():
                raise ValueError("age must contain only digits.")
            age = int(age)
            if age <= 0 or age >= 130:
                raise ValueError ("age must be between 0 and 130.")
            with open('Names.txt', 'a', encoding='utf-8') as new_file:
                report = f"Name is {name}\nAge is {age}\n"
                new_file.write(report)
            return f"hello, {name}! Age is {age}"
        except ValueError as ve:
            return str(ve)
# name_age_v2('Baiden', '98')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 3<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# while True:
#     try:
#         amount = int(input(f"An amount must be multiple to 10 limit is 1000\nEnter your amount: "))
#         if amount > 1000 or amount % 10:
#             raise ValueError("Amount must be <= 1000 and divisible by 10.")
#         print(f"${amount} withdraw.")
#         break
#     except ValueError as ve:
#         print("Invlid input:",ve)
#     finally:
#         print("Transaction complete.\n")

numbers = [1,2]
# while True:
#     try:
#         user_input = input("Enter a positive number, enter done to exit: ")
#         # if user_input.endswith('done'):
#         if user_input == 'done':
#             break
#         user_input = int(user_input)
#         if user_input < 0:
#             raise ValueError("Number must greater than ZERRRRROOOOO@!!!!11")
#         numbers.append(user_input)
#     except ValueError as ve:
#         print("Invalid input:",ve)
# print(sum(numbers))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 4<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# def total_list(lst):
#     total = 0
#     for num in lst:
#         if num < 0:
#             raise ValueError("Number must greater than ZERRRRROOOOO@!!!!11")
#         total += num
#     return total
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 5<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu():
    print(str('>>>> MENU <<<<<').center(70))
    print(str("\nSelect an option from the list please. Type done to exit"))
    print("\n\t1. Show whole list.\n\t2. Get the biggest number.\n\t3. Get the smallest\n\t4. Search by index.\n\t5. Delete by index.\n\t6. Exit\n")

def task5():

    while True:
        user_input = input("Enter a positive number, or 'done' to finish: ")
        if user_input == 'done':
            break
        try:
            num = int(user_input)
            if num < 0:
                raise ValueError("Only positive numbers allowed")
            numbers.append(num)
        except ValueError as e:
            print("Invalid input:", e)

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            print("List:", numbers)

        elif choice == '2':
            print("Max:", max(numbers))

        elif choice == '3':
            print("Min:", min(numbers))

        elif choice == '4':
            try:
                index = int(input("Enter index: "))
                print("Value:", numbers[index])
            except (IndexError, ValueError):
                print("Invalid index!")

        elif choice == '5':
            try:
                index = int(input("Enter index to delete: "))
                del numbers[index]
                print("Updated list:", numbers)
            except (IndexError, ValueError):
                print("Invalid index!")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid menu option.")

task5()











#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TASK 6<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# try:
#     print("Sum:", total_list(numbers))
# except ValueError as e:
#     print("ERROR OUTSIDE:", e)








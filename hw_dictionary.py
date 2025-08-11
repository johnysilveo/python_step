
#>>>>>>>>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<<<<<<<<<<<

eng_fr_dict = {}

def dicti_eng_frank():
    while True:
        print("\n--- English-French Dictionary ---")
        print("1. Add word")
        print("2. Delete word")
        print("3. Find translation")
        print("4. Update translation")
        print("5. Show all")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            eng = input("English word: ")
            fr = input("French translation: ")
            eng_fr_dict[eng] = fr
        elif choice == '2':
            eng = input("Word to delete: ")
            if eng in eng_fr_dict:
                del eng_fr_dict[eng]
            else:
                print("La pupee monte le son.")
        elif choice == '3':
            eng = input("Word to find: ")
            print(eng_fr_dict.get(eng, "Translation not found."))
        elif choice == '4':
            eng = input("Word to update: ")
            if eng in eng_fr_dict:
                fr = input("New translation: ")
                eng_fr_dict[eng] = fr
            else:
                print("Word not found.")
        elif choice == '5':
            print(eng_fr_dict)
        elif choice == '0':
            break
        else:
            print("Invalid option.")

# dicti_eng_frank()

#>>>>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<


employees = {}

def company():
    while True:
        print("\n--- Company Menu ---")
        print("1. Add employee")
        print("2. Delete employee")
        print("3. Find employee")
        print("4. Update employee info")
        print("5. Show all employees")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            name = input("Full Name: ")
            phone = input("Phone: ")
            email = input("Corporate Email: ")
            position = input("Position: ")
            office = input("Office Number: ")
            skype = input("Skype: ")
            employees[name] = {
                "Phone": phone,
                "Email": email,
                "Position": position,
                "Office": office,
                "Skype": skype
            }
        elif choice == '2':
            name = input("Employee to delete: ")
            if name in employees:
                del employees[name]
            else:
                print("Not found.")
        elif choice == '3':
            name = input("Employee to find: ")
            print(employees.get(name, "Not found."))
        elif choice == '4':
            name = input("Employee to update: ")
            if name in employees:
                field = input("Which field (Phone, Email, Position, Office, Skype): ")
                if field in employees[name]:
                    new_val = input("New value: ")
                    employees[name][field] = new_val
                else:
                    print("Invalid field.")
            else:
                print("Employee not found.")
        elif choice == '5':
            for name, info in employees.items():
                print(f"{name}: {info}")
        elif choice == '0':
            break
        else:
            print("Invalid option.")

# company()

#>>>>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<


def merge():
    d1 = {'a': 5, 'b': 3}
    d2 = {'b': 2, 'c': 4}
    print("Dictionary 1:", d1)
    print("Dictionary 2:", d2)
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    print("Merged dictionary:", merged)

# merge()

#>>>>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<

def word():
    text = input("Enter a text: ")
    words = text.lower().split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    for word, count in word_dict.items():
        print(f"{word}: {count}")

# word()


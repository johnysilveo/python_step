



eng_to_spanish = {}
def add_new_word():
    while True:
        print("\n\t\tHere you can add a new word to your dictionary.")
        print('\n\t\tInstructions')
        print("You can add as many words as you want. No limits")
        print('For exit type "exit"')
        key = input('Enter an english word: ').lower()
        if key == 'exit':
            break
        value = input('Enter a spanish translation: ').lower()
        eng_to_spanish[key] = value

def delete_word():
    while True:
        print('\n\t\t Here tou can delete a word and translation\n\t\t by simply entering an english word')
        print("Instructions")
        print("You can delete as many words as you want. No limits")
        print('For exit type "exit"')
        key_to_delete = input("Enter an english word you would like to delete: ").lower()
        if key_to_delete == 'exit':
            break
        del eng_to_spanish[key_to_delete]
        print(f"Word {key_to_delete} is deleted")

def accessing_words():
    while True:
        print('\n\t\t Here you can access the words you want.')
        print("Instructions")
        print("You can access as many words as you want. No limits")
        print('For exit type "exit"')
        key_to_access = input("Enter an english word you would like to translate: ").lower()
        if key_to_access == 'exit':
            break
        if key_to_access in eng_to_spanish:
            print(f"Word '{key_to_access}' is translated to '{eng_to_spanish[key_to_access]}'")
        else:
            print(f"Word '{key_to_access}' not found. Try again.")

def change_word():
    while True:
        print('\n\t\t Here you can change the words you want.')
        print("Instructions")
        print("You can change as many words as you want. No limits")
        print('For exit type "exit"')
        key_to_change = input("Enter an english word: ").lower()
        if key_to_change == 'exit':
            break
        elif key_to_change in eng_to_spanish:
            eng_to_spanish[key_to_change] = eng_to_spanish[key_to_change]








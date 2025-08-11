#>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<<<<
test = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, \nwhen an unknown printer took a galley of type and scrambled it to make a type \nspecimen book. It has survived not only five centuries"

def counts(str1):
    print(len(str1))

#>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<

def print_each():

    str2 = input("Enter your text: ")
    for o in str2[:]:
        print(o)

    counts(str2)

#>>>>>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<<<<

def count_upper():
    count = 0
    for i in test:
        if i.isupper():
            count += 1

    print(f"Uppercase letters in text is: {count}")

#>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<

str4 = input("ENTER: ")
sent = str4.count('.') + str4.count('!') + str4.count('?')
print(f"Number of sentences in the text is: {sent}")
counts(str4)
#>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<

str5 = input("Enter a word: ")
str5c = str5.lower().replace(" ", "")
str5r = str5c[::-1]

if str5c == str5r:
    print("Ts is a palindrome.")
else:
    print("It is not a palindrome.")

#>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<

reserve = 'dick', 'pussy', 'ass', 'fuck', 'bitch'
str6 = input("Enter text: ")
for word in reserve:
    if word in str6:
        str6 = str6.replace(word, word.upper())
        
print(str6)

#>>>>>>>>>>>>>>>>>>>TASK 7<<<<<<<<<<<<<<<<<<<<<<<<<<

str7 = input(f"\nEnter text: ")
start = input(f"\nEntar start symbol: ")
end = input(f"\nEnter end symbol: ")
startx = int(str7.find(start))
endx = int(str7.find(end))
if startx != -1 and endx != -1:
   print(str7[0:startx] + str7[endx+1:])
else:
    print("ERROR")










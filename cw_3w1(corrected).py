sometext = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, \nwhen an unknown printer took a galley of type and scrambled it to make a type \nspecimen book. It has survived not only five centuries"  # multiline text

print(sometext)  # print full text

text = "hello"  # define string
btext = text.encode("utf-8")  # encode to UTF-8 bytes
print(btext.decode('utf-8'))  # decode back to string
print(id(text))  # print memory ID of string
text = "helo"  # modify string
print(id(text))  # print new memory ID (changed object)

str1 = "part1, "
str2 = "part2"
print(str1 + str2)  # concatenate strings
print(str1 * 3)  # repeat string 3 times

# This is indexing
name = "user1"
print(name[0])  # print character at index 0
print(name[1])  # print character at index 1
print(name[2])  # print character at index 2
print(name[3])  # print character at index 3
print(name[4])  # print character at index 4

# Count how many characters are in the string
print(len(name))  # length of the string

print(sometext)  # print text again

# String case methods
print(sometext.capitalize())  # first letter capitalized, rest lowercase
print(sometext.lower())  # all lowercase
print(sometext.upper())  # all uppercase
print(sometext.title())  # first letter of each word uppercase
print(sometext.swapcase())  # switch upper to lower and vice versa

print(sometext.count("Lorem"))  # count how many times "Lorem" appears
print(sometext.find("took", 10))  # find "took" starting from index 10
print(sometext.find("Lorem", 10))  # find "Lorem" starting from index 10
print(sometext.rfind("Lorem"))  # find last occurrence of "Lorem"

print(sometext.startswith('Lorem'))  # check if text starts with "Lorem"
print(sometext.endswith("centuries"))  # check if text ends with "centuries"

text = "1   2   3"
print(text.isalnum())  # True if all characters are letters/numbers
print(text.isdigit())  # True if all characters are digits
print(text.islower())  # True if all letters are lowercase
print(text.isupper())  # True if all letters are uppercase
print(text.strip())        # Removes leading and trailing whitespace
print(text.lower())        # Converts all characters to lowercase
print(text.upper())        # Converts all characters to uppercase
print(text.replace("a", "b"))  # Replaces all "a" with "b"
print(text.split(","))     # Splits string into list by commas
print(",".join(["a", "b"]))# Joins list into string with commas
print(text.find("a"))      # Returns index of first "a", or -1
print(text.startswith("Hi"))  # True if text starts with "Hi"
print(text.endswith("!"))  # True if text ends with "!"

print(text.isalpha())      # True if all characters are letters
print(text.isdigit())      # True if all characters are digits
print(text.isalnum())      # True if all characters are letters or digits
print(text.isdecimal())    # True if all characters are base-10 digits
print(text.isnumeric())    # True if all characters are numeric (incl. Unicode)
print(text.title())        # Capitalizes first letter of each word
print(text.capitalize())   # Capitalizes first character of the string
print(text.count("a"))     # Counts how many times "a" appears
print(text.index("a"))     # Index of first "a" (or error if not found)
print(text.rfind("a"))     # Index of last occurrence of "a"
print(text.lstrip())       # Removes leading whitespace
print(text.rstrip())       # Removes trailing whitespace
print(text.casefold())     # Aggressively lowercases for caseless comparison
print(text.swapcase())     # Swaps letter case
print(text.zfill(10))      # Pads string on left with zeros to reach length 10
print(text.center(50))     # Centers text in a 50-character field
print(text.ljust(50))      # Left-aligns in 50 characters
print(text.rjust(50))      # Right-aligns in 50 characters
print(text.partition(":")) # Splits into (before, sep, after)
print(text.rpartition(":"))# Splits from the right (before, sep, after)

# TEXT FORMATTING
print(text.center(40, '$'))  # center the string, pad with '$' to length 40
print(text.lstrip())  # remove spaces on the left
print(text.rstrip())  # remove spaces on the right
print(text.strip())  # remove spaces on both sides
print(text.isalpha()) #

print("--------------------------")
for s in text:
    print(s.isspace())  # check if character is a whith space

print(text.replace(" ", '_', 5))  # replace first 5 spaces with underscores

myStr = "pythin cool"
print(myStr[0:6])  # slice from index 0 to 5
print(myStr[6:])  # slice from index 6 to end
print(myStr[-5:11])  # slice from -5 to index 11
print(myStr[-5])  # single character at -5 index
print(myStr[::-1]) # reverse the text

text = input("Enter a string: ")  # user input string

# Search and replace part
search_word = input("Enter the word to search for: ")  # word to find
replace_word = input("Enter the replacement word: ")  # word to insert
new_text = text.replace(search_word, replace_word)  # do the replacement
print("Updated string:", new_text)  # print updated string

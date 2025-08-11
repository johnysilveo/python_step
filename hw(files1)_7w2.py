import pickle
from itertools import zip_longest


# text1 = 'The morning sun rose slowly over the quiet valley. Birds chirped softly in the trees as dew sparkled on the grass. A gentle breeze drifted through the air, carrying the scent of fresh pine. Peace settled in the silence, broken only by the rustle of distant footsteps approaching.'
# this is are two texts that i created files for like so open with('text11','wb') as file: pickle.dump(text1,file) and the same for second one.
# text2 = 'As sunlight crept across the silent hills, the breeze carried whispers through tall trees. Morning dew clung to every leaf, glistening like tiny stars. In the hush, birds sang low and steady. Footsteps echoed faintly in the distance, a reminder that even stillness can hold the promise of movement.'
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 1<<<<<<<<<<<<<<<<<<<<<<<<<<<<
with open('text11.txt','rb') as file1, open('text22.txt','rb') as file2:
    data1 = pickle.load(file1)
    data2 = pickle.load(file2)
    words1 = data1.split()
    words2 = data2.split()
for i, (word1, word2) in enumerate(zip_longest(words1,words2, fillvalue = '---missing---'), start=1):
    if word1 != word2:
                print(f'Mismatch at line {i}:')
                print('File1:', word1)
                print('File2:', word2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 1 but shows exact matching<<<<<<<<<<<<<<<<<<<<<<<<<<<<

with open('text11.txt','rb') as file1, open('text22.txt','rb') as file2:
    data1 = pickle.load(file1)
    data2 = pickle.load(file2)
    words1 = data1.split()
    words2 = data2.split()
match_count = 0
for i, (line1, line2) in enumerate(zip_longest(words1,words2, fillvalue = '---missing---'), start=1):
    if line1 == line2:
        match_count += 1
print(f"Total exact matches: {match_count}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<

try:
    with open('text11.txt', 'rb') as file:
        data1 = pickle.load(file)
        # print(repr(data1))
        if isinstance(data1, dict):
            data2 = data1['text']
        words_check= data2.split()
        vowels = 0
        consonants = 0
        digit = 0
        line_count = len(data2.splitlines())
        leters = len(data2)
        words = len(words_check)
        for char in data2:
            if char.lower() in 'aeiou':
                vowels += 1
            elif char.isalpha():
                consonants +=1
            elif char.isdigit():
                digit += 1
        report = (
            f"rows = {line_count}\n"
            f"leters = {leters}\n"
            f"words = {words}\n"
            f"vowels = {vowels}\n"
            f"consonants = {consonants}\n"
            f"digits = {digit}\n"
        )
    with open('report.txt', 'a', encoding='utf-8') as backup:
        backup.write(report)
        print('ur report is ready')
except Exception as ex:
    print("an error has occurred in the process:", ex)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 3<<<<<<<<<<<<<<<<<<<<<<<<<<<<

with open('text11.txt','rb') as file:
    content = pickle.load(file)
    splited = content.splitlines()
    if len(splited) > 1:
        new_lines = splited[:-1]
    else:
        new_lines = []

    result = '\n'.join(new_lines)
with open('report.txt', 'a', encoding='utf-8') as backup:
    print("Number of lines:", len(splited))
    print("Result:", repr(result))

    backup.write(">>>>>>>>Task 3<<<<<<<<<\n")
    backup.write(result + '\n')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 4<<<<<<<<<<<<<<<<<<<<<<<<<<<<

with open('report.txt','r',encoding='utf-8') as file:
    content = file.read()
    splited = content.splitlines()
    # longest = max(len(line) for line in splited)
    longest = 0
    for line in splited:
        length = len(line)
        if length > longest:
            longest = length

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 5<<<<<<<<<<<<<<<<<<<<<<<<<<<<

with open('text11.txt','rb') as file:
    data = pickle.load(file)
    user_word = input('Enter word to count: ')
    result = data.count(user_word)
    print(f"The word '{user_word}' appears {result} times.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 6<<<<<<<<<<<<<<<<<<<<<<<<<<<<

with open('text11.txt','rb') as file:
    data = pickle.load(file)
    user_word1 = input('Enter word to change: ')
    user_word2 = input('Enter word to change with: ')
    result = data.replace(user_word1,user_word2)
    print(f"The word '{user_word1}' replaced with {user_word2}.")
with open('updated_text.txt', 'w', encoding='utf-8') as file:
    file.write(result)

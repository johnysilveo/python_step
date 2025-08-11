# import pickle
#
# # Create a dictionary object
simple_object = dict(int_nums=[1, 2, 3, 4, 5], text="test", number=6.5, boolean=True)
#
# # Serialize and save to file
# with open('text.txt', 'wb') as file:              # open in write-binary mode
#     pickle.dump(simple_object, file)              # save the object into the file
#
# # Load (deserialize) the object from file
# with open('text.txt', 'rb') as file:              # open in read-binary mode
#     deserialize_object = pickle.load(file)             # read and decode the object
#
# # Print the restored object
# print(deserialize_object)
#
# #Напишіть програму, яка відкриває файл numbers.txt,
# # читає числа з нього та обчислює їхню суму, потім записує результат у sum.txt.
# # 2 Напишіть програму, яка запитує у користувача ім'я файлу і слово, потім
# # підраховує кількість входжень цього слова у файлі і виводить результат.
# total = 0
#
# with open('numbers.txt','r',encoding='utf-8') as file:
#     for num in file:
#         total += int(num.strip())
#
#
# with open('sum.txt', 'w', encoding='utf-8') as out_file:
#     out_file.write(str(total))
#
# file_name = input('Enter file name: ')
# search_for = input('Enter word to search: ')
#
# with open(file_name, 'r', encoding='utf-8') as file:
#     content = file.read()
#     count = content.count(search_for)
#     print(f"The word '{search_for}' appears {count} times.")
#
# numbers = list(map(int, input('Enter numbers separated by space: ').split()))
#
# with open('numbers.pkl', 'wb') as file:
#     pickle.dump(numbers, file)
#
# with open('numbers.pkl', 'rb') as file:
#     deserialize_object = pickle.load(file)
#

import json


with open('test_json.json', 'w',) as file:
    json.dump(simple_object, file)
with open('test_json.json','r') as file:
    data = json.load(file)
print(data)




music_dict = {
    'Liquid Stranger': ['Robot Rox'],
    'Borgore':['Ice Cream']
}

def write_json_file(file_to_write,dict_to_write):
    # file_to_write += '.json'
    with open(file_to_write,'w') as file:
        data = json.dumps(dict_to_write,indent=4)
        file.write(data)

def read_json_file(file_to_read):
    # file_to_read += '.json'
    with open(file_to_read,'r') as file1:
        dict_from_file = json.loads(file1.read())
    return dict_from_file


def add_info(file,band,song):
    dict_from_file = read_json_file(file)
    band_name = list(dict_from_file.keys())
    if band in band_name:
        dict_from_file[band] = [dict_from_file[band], song]
        print(dict_from_file)


    else:
        dict_from_file[band] = [song]
    write_json_file(file,dict_from_file)


add_info('music.json', 'Baby Lasagna','Rim Tigi Dim')
write_json_file('music',music_dict)
read_json_file('music')
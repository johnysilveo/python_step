#          DICTIONARY
from operator import truediv

#book_dict = {'key1':"book1"}


my_dict = dict([('a',111),('b',222)])

# print(book_dict)
# print(my_dict)
# print(type(book_dict))

key_list = ['a','b']
value_list = [111,222]
new_dict = dict(zip(key_list, value_list))
print(new_dict)

book_dict = {'author':"python",
             'title': 'Gvido',
             'price': 200,
             'language': 'en'}
new_dict2 = dict(first_name='Joe', last_name ='Smoth')
# print(len(book_dict))
# print(book_dict['title'])

book_dict['price'] = 3003
# del book_dict['price']
print(book_dict)

# for key in book_dict:
#     print(key, book_dict[key])
#
# for key,value in book_dict.items():
#     print(key,value)

# new_info = input('What info about the book to add? ')
# if new_info != '':
#     new_value = input('Input value: ')
#     if new_value != '':
#         if new_info not in book_dict:
#             book_dict[new_info] = new_value
#             print(book_dict)
#         else:
#             print('sure?')
#     else:
#         print('No value for this key')
# else:
#     print('No key')

print(book_dict.get('price', 0))

book_dict.update([('test1',1), ('test2',2)])
print(book_dict)

book_dict.pop('test1')
book_dict.pop('test111', 'none')
print(book_dict.popitem())
copy_book = book_dict.copy()
print(copy_book)


users = [
    {'name': 'Olivia','age':20,'login':'user11'},
    {'name': 'Johny', 'age': 32, 'login': 'user12'},
    {'name': 'Columbus', 'age': 657, 'login': 'user13'},
    {'name': 'Baiden', 'age': 98, 'login': 'user14'},
]

key_name = 'name'
key_value = 'Olivia'

def find_user(users, key_name, key_value):
    is_elem_found = False

    for user in users:
        if user.get(key_name) == key_value:
            print("Element is found1")
            for key,value in user.items():
                print(f"{key} - {value}")
            is_elem_found = True
            return user
    if not is_elem_found:
        print("Element is not found!")

find_user(users, 'name', 'Olivia')

film_dict = {'title': ' Godzilla',
             'creator':'Spilberg',
             'rate': 8.5,
             'description':'Good film',
             'years': [2010,2011]
             }

for key,value in film_dict.items():
    print(key,value)

key_list = list(film_dict.keys())
print(key_list)
sorted_keys = sorted(key_list)
print(sorted_keys)

for key in sorted_keys:
    print(f'{key}{film_dict[key]}')


sorted_by_name = sorted(users,key=lambda x: x['age'])
print('User list is sorted in order of age.')
for user in sorted_by_name:
    for key,value in user.items():
        print(key,value)

user18 = list(filter(lambda user: user['age'] >= 98, users))
for user in user18:
    for key,value in user.items():
        print(key,value)

countries = ['Ukraine','France','Japan','USA']
capitals = ['Kyiv','Paris','Tokyo','Washington']

def find_c(country_dict, country_name):
    if country_name in country_dict:
        print("Element is found!")
        print(f"{country_name} - {country_dict[country_name]}")
        return country_dict[country_name]
    else:
        print("Element is not found!")

def add_country(country_dict):
    country_name = input("Enter country: ")
    if country_name in country_dict:
        print("Country already exists.")
    else:
        capital = input("Enter capital: ")
        country_dict[country_name] = capital
        print("Pair added!")

country_dict = dict(zip(countries, capitals))
add_country(country_dict)
print(country_dict)

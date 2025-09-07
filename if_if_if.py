

alien_color = 'yellow'


if alien_color == 'red':
    print('you get 5 points')
if alien_color == 'green':
    print('you get 10 points')
if alien_color == 'yellow':
    print('you get -666 points')

if alien_color == 'green':
    print('you get 5 points')
else:
    print('you get 10 points')

if alien_color == 'green':
    print('you get 5 points')
elif alien_color == 'yellow':
    print('you get -666 points')
else:
    print('you get 10 points')


age = 3

if age < 2:
    print('person is a baby')
elif 2 <= age < 5:
    print('person is a toddler')
elif 5 <= age < 13:
    print('person is a kid')
elif 13 <= age < 20:
    print('person is a teenager')
elif 20 <= age < 65:
    print('person is an adult')
else:
    print('person is elder')

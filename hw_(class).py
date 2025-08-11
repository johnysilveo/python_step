import datetime


# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Додати метод is_major, який повертає True, якщо людина повнолітня (більше або одно 18 років) інакше False.




class Human:
    def __init__(self,name,surname,dob,address,country,phone):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.country = country
        self.phone = phone

    def __str__(self):
        return f"Human's name is {self.name} and it's last name is {self.surname}\nDOB is {self.dob}\nAddress is {self.address}\nPhone: {self.phone}\nCountry: {self.country}"

    def input_data(self):
        self.name = input("Enter ur name: ")
        self.surname = input("Enter ur last name: ")
        self.dob = input("Enter ur DOB like so mm/dd/yyyy: ")
        self.address = input("Enter ur address: ")
        self.country = input("Enter your country: ")
        self.phone = input("enter ur phone number: ")

    # def is_major(self):
    #     dob_date = datetime.datetime.strptime(self.dob, "%m/%d/%Y")
    #     return (datetime.now().year - dob.year) >= 18

    def is_major(self):
        dob_year = int(self.dob.split('/')[-1])
        if dob_year <= 2007:
            return True
        else:
            return True

# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста, назву регіону, назву країни, кількість жителів у місті, поштовий індекс міста,
# телефонний код міста. Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Написати метод is_valid_zipcode, який повертає True якщо __zipcode містить 5 цифр.

class City:

    def __init__(self,name,state,country,area_code,pop,zip_code):
        self.name = name
        self.state = state
        self.area_code = area_code
        self.pop = pop
        self.country = country
        self.zip_code = zip_code

    def __str__(self):
        return f"The city of {self.name} in {self.state} at country {self.country} with population of {self.pop} people and area code with zip is {self.area_code},{self.zip_code}"

    def input_data(self):
        self.name = input("Enter name of the city: ")
        self.state = input("Input name if the state: ")
        self.area_code = input("Enter area code: ")
        self.pop = input("Enter population of the city: ")
        self.country = input("Enter name of the country: ")
        self.zip_code = input("Enter your zip code: ")

    def valid_zip(self):
        return self.zip_code.isdigit() and len(self.zip_code) == 5

# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни, назву континенту, кількість жителів країни, телефонний код країни, назву столиці,
# назву міст країни. Реалізуйте методи класу для введення-виведення даних та інших операцій.
#


class Country:

    def __init__(self,name,cont,city,area_code,pop,capital):
        self.name = name
        self.cont =cont
        self.area_code = area_code
        self.pop = pop
        self.city = city
        self.capital = capital

    def __str__(self):
        return f"The country of {self.name} on continent {self.cont} with are code {self.area_code} and population of {self.pop} people the capital is {self.capital} and another city is {self.city}"

    def input_data(self):
        self.name = input("Enter name of the country: ")
        self.cont = input("Input continent: ")
        self.area_code = input("Enter area code: ")
        self.pop = input("Enter population of the country: ")
        self.city = input("Enter name of the second large city: ")
        self.capital = input("Enter your capital: ")

        # Завдання 4
        # Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
        # Реалізуйте методи класу для введення-виведення даних та інших операцій.
        #

class Automobil:
    def __init__(self,model,year,make,engine,color,price):
        self.model = model
        self.year = year
        self.make = make
        self.engine = engine
        self.color = color
        self.price = price

    def __str__(self):
        return f"Model {self.model}, make {self.make}, year {self.year}, engine {self.engine}, color is {self.color} and the price {self.price}"

    def input_data(self):
        self.model = input("enter madel name: ")
        self.year = input("enter year:")
        self.make = input("enter make of the car: ")
        self.engine = input("enter engine size in liters: ")
        self.color = input("enter color: ")
        self.price = input("enter price: ")

    #
    # Завдання 5
    # Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
    # Реалізуйте методи класу для введення-виведення даних та інших операцій.
    #

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: '{self.title}' by {self.author} ({self.year})\nGenre: {self.genre}, Publisher: {self.publisher}, Price: ${self.price}"

    def input_data(self):
        self.title = input("Enter book title: ")
        self.year = input("Enter year of publication: ")
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = input("Enter price: ")



#
#
# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @property
#     def color(self):
#         return self.__color
#
#     def __str__(self):
#         return f"Cat: {self.name}, Age: {self.age}, Color: {self.color}"
#
#
# class Dog:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @property
#     def color(self):
#         return self.__color
#
#     def __str__(self):
#         return f"Dog: {self.name}, Age: {self.age}, Color: {self.color}"
#
#
# # --- Create and Print ---
# cat1 = Cat("Whiskers", 3, "gray")
# dog1 = Dog("Rex", 5, "brown")
#
# print(cat1)
# print(dog1)


class Animal:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}, Color: {self.color}"

    def sound(self):
        print('meaow')

class Cat(Animal):
    def __init__(self,name,age,color,claw):
        super().__init__(name,age,color)
        self.claw = claw



class Dog(Animal):
    pass  # Inherits everything from Animal

class Cow(Animal):
    def __init__(self,name,age,color,fang):
        super().__init__(name,age,color)
        self.fang = fang

# --- Create and Print ---
cat1 = Cat("Whiskers", 2, "white",False)
dog1 = Dog("Bruno", 4, "black",
           )
cow1 = Cow('Burenka', 7, 'black and white')
print(cat1)
print(dog1)
print(cow1)

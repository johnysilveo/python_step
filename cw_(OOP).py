import random



class Cat:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self.age

    @property
    def color(self):
        return self.color


class Student:
    # age = 20
    # name = "Bob"
    # public prop
    spec = "Computer science"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__avgMark = 0
        # private prop
        self.__personId = random.randint(1, 100)

    def showInfo(self):
        return f"Student {self.name}, age {self.age}, id: {self.__getID()}"

    # private method
    def __getID(self):
        return self.__personId

    @property
    def avgMark(self):
        return self.__avgMark

    @avgMark.setter
    def avgMark(self, mark):
        self.__avgMark = mark


# st2 = Student()
# st2.age = 27
# print(st2.age, st2.name)
#
# st1 = Student()
# print(st1.age, st1.name)

st3 = Student("Bob", 30)
st3.name = "Bill"
print(st3.showInfo(), st3.spec)
st3.avgMark = 9
print(st3.avgMark)

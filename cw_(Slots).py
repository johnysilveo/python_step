class Human:
    __slots__ = ('name','gender','age')

    def __init__(self,name):
        self.name = name

human = Human('bill')
human.age = 20
print(human.name, human.age)

# human.salary = 100

# print(human.__dict__)

class Student(Human):
    __slots__ = ('marks',)

    def __init__(self, name):
        super().__init__(name)
        self.marks = []
        self.age = 0


st = Student('Norman')
st.age = 21
st.marks.append(95)

print(st.name, st.age, st.marks)



from abc import ABC, abstractmethod



class BaseABC(ABC):
    def test(self):
        print('test')

    @abstractmethod
    def showabc(self):
        pass




class Usually(BaseABC):
    def showabc(self):
        print("Fucking working")

abc = Usually()
abc.showabc()

# baseabc = BaseABC()

class Abstract_Base_Player(ABC):
    def __init__(self,name,rasa):
        self.nama = name
        self.rasa = rasa

    def show_info(self):
        print(f"name:{self.nama},rasa: {self.rasa}")

    @abstractmethod
    def attack(self):
        pass

class Human(Abstract_Base_Player):
    def __init__(self,name,age):
        super().__init__(name,'human')
        self.age = age

    def attack(self):
        print(f"I am {self.rasa} and i attack with a sword bitch!")

    def show_info(self):
        super().show_info()
        print(f"age: {self.age}")


class Moron(Abstract_Base_Player):
    def __init__(self, name, age):
        super().__init__(name, 'ruski')
        self.age = age

    def attack(self):
        print(f"I am {self.rasa} and ya ataku s moey srakoy!")

    def show_info(self):
        super().show_info()
        print(f"age: {self.age}")


human1 = Human('Artur',50)
human1.show_info()
human1.attack()

class Game:
    def __init__(self):
        self.players = []

    def add_player(self,*args):
        for new_player in args:
            if isinstance(new_player, Abstract_Base_Player):
                self.players.append(new_player)
            else:
                print("erroe")

    def show_players(self):
        if self.players:
            for player in self.players:
                player.show_info()
            else:
                print('no players')

    def fight(self):
        pass

pidor = Moron('rusnya',140)

new_game = Game()
new_game.add_player(human1, pidor)
new_game


class Pet:
    def __init__(self,name,animal,age):
        self.name = name
        self.animal = animal
        self.age = age

    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def show_name_pet(self):
        pass
    @abstractmethod
    def type(self):
        pass

class Cat(Pet):

    def sound(self):
        print('mur mur')

    def show_name_pet(self):
        print(f'name is {self.name}')

    def type(self):
        print(f'hello iam a {self.animal}')


class Parrot(Pet):

    def sound(self):
        print('whatever u say')

    def show_name_pet(self):
        print(f'name is {self.name}')

    def type(self):
        print(f'hello iam a {self.animal}')


class Dog(Pet):

    def sound(self):
        print('Gav gav')

    def show_name_pet(self):
        print(f'name is {self.name}')

    def type(self):
        print(f'hello iam  {self.animal}')


class Shape:
    def __init__(self,length, hight):
        self.length = length
        self.hight = hight

    @abstractmethod
    def area(self):
        pass

















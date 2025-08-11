class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return 'gav'

class Cat(Animal):
    def speak(self): return ' meaow'

class AnimalFactory:
    def create_animal(self,animal_type):
        if animal_type == 'dog' :
            return Dog()
        elif animal_type == 'cat':
            return Cat()

factory = AnimalFactory()
pet = factory.create_animal('dog')
print(pet.speak())
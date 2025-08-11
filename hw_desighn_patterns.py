from abc import ABC,abstractmethod
import pickle


class Car:
    def __init__(self,make,body_type,color,engine_size,door_count,options,model,powertrain):
        self.powertrain = powertrain
        self.make = make
        self.body_type = body_type
        self.color = color
        self.engine_size = engine_size
        self.door_count = door_count
        self.options = options
        self.model = model

    def show_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Body Type: {self.body_type}")
        print(f"Color: {self.color}")
        print(f"Powertraine: {self.powertrain}")
        print(f"Engine: {self.engine_size}")
        print(f"Doors: {self.door_count}")
        print(f"Options: {self.options}")

class CarBuilder(ABC):
    @abstractmethod
    def set_make(self): pass
    @abstractmethod
    def set_model(self): pass
    @abstractmethod
    def set_body_type(self): pass
    @abstractmethod
    def set_color(self): pass
    @abstractmethod
    def set_engine_size(self): pass
    @abstractmethod
    def set_door_count(self): pass
    @abstractmethod
    def set_options(self): pass
    @abstractmethod
    def show_info(self): pass
    @abstractmethod
    def set_powertrain(self): pass

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car(None,None, None, None, None, None, None, None)
    def set_make(self):
        self.car.make = 'Lexus'
    def set_model(self):
        self.car.model = "LS 500"
    def set_body_type(self):
        self.car.body_type = 'Convertable'
    def set_color(self):
        self.car.color = 'Black'
    def set_powertrain(self):
        self.car.powertrain = "Gasoline"
    def set_engine_size(self):
        self.car.engine_size = 5.0
    def set_door_count(self):
        self.car.door_count = 2
    def set_options(self):
        self.car.options = ["HUD", "Leather", "Mark Levinson"]
    def show_info(self):
        return self.car

class Director:
    def __init__(self,builder:CarBuilder):
        self.builder = builder

    def build_car(self):
        self.builder.set_make()
        self.builder.set_model()
        self.builder.set_color()
        self.builder.set_body_type()
        self.builder.set_powertrain()
        self.builder.set_engine_size()
        self.builder.set_door_count()
        self.builder.set_options()
        return self.builder.show_info()

builder = SportsCarBuilder()
director = Director(builder)
sports_car = director.build_car()
sports_car.show_info()


#past 1. Makaroni, ChikParm, Carbonara
# type, sauce,filling,toppings,info

class Pasta():
    def __init__(self,pasta_type,sauce,filling,toppings):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.filling = filling
        self.toppings = toppings
    def show_info(self):
        print(f"Pasta type is: {self.pasta_type}")
        print(f"Sauce is: {self.sauce}")
        print(f"Filling: {self.filling}")
        print(f"Toppings are: {self.toppings}")

class PastaBuilder(ABC):
    @abstractmethod
    def set_pasta_type(self): pass
    @abstractmethod
    def add_sauce(self): pass
    @abstractmethod
    def add_fillings(self): pass
    @abstractmethod
    def add_toppings(self): pass
    @abstractmethod
    def show_info(self): pass

class MakaroniPastaBuilder(PastaBuilder):
    def __init__(self):
        self.makaroni = Pasta(None,None,None,None)
    def set_pasta_type(self):
        self.makaroni.pasta_type = 'Макарони'
    def add_sauce(self):
        self.makaroni.sauce = "Кетчуп 'Торчин"
    def add_fillings(self):
        self.makaroni.filling = "Сосиски дитячі вершкові"
    def add_toppings(self):
        self.makaroni.toppings = "Клуб сиру Вітяз"
    def show_info(self):
        return self.makaroni

class Director1:
    def __init__(self,builder:PastaBuilder):
        self.builder = builder
    def make_a_pasta(self):
        self.builder.set_pasta_type()
        self.builder.add_sauce()
        self.builder.add_fillings()
        self.builder.add_toppings()
        return self.builder.show_info()

builder = MakaroniPastaBuilder()
director = Director1(builder)
pasta = director.make_a_pasta()
pasta.show_info()


# Singleton for loging:)

class InputNumbers:
    def __init__(self,user_data):
        self.user_data = user_data
    @staticmethod
    def get_data():
        user_data = input("Enter numbers: ")
        return user_data

class InputPath():
    def __init__(self,path):
        self.path = path
    @staticmethod
    def get_path():
        path = input("Enter path to the file: ")
        return path

class ConsolManager:
    _instance = None
    def __init__(self):
        if ConsolManager._instance is not None:
            raise Exception("Only one insatnce of class")
        else:
            ConsolManager._instance = self
    @staticmethod
    def get_instance():
        if ConsolManager._instance is None:
            ConsolManager()
        return ConsolManager._instance
    def log(self,msg):
        with open(f"{InputPath.get_path()}",'r',encoding='utf-8')as file:
            content = file.read()
# i stped on making opening file by the path. ask for the way how it is implemnted


log_manager = ConsolManager.get_instance()
log_manager.log('Singleton pattern is returned')
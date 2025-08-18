from abc import ABC, abstractmethod


# ================= CAR =================

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
        print(f"Powertrain: {self.powertrain}")
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
        self.car = Car(None,None,None,None,None,None,None,None)
    def set_make(self):
        self.car.make = f'Lexus'
    def set_model(self):
        self.car.model = "LS 500"
    def set_body_type(self):
        self.car.body_type = 'Convertible'
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

class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car(None,None,None,None,None,None,None,None)
    def set_make(self):
        self.car.make = f'Toyota'
    def set_model(self):
        self.car.model = "RAV 4"
    def set_body_type(self):
        self.car.body_type = 'SUV'
    def set_color(self):
        self.car.color = 'Red'
    def set_powertrain(self):
        self.car.powertrain = "Gasoline"
    def set_engine_size(self):
        self.car.engine_size = 2.0
    def set_door_count(self):
        self.car.door_count = 5
    def set_options(self):
        self.car.options = ["Heated sits", "Leather interior", "JBL"]
    def show_info(self):
        return self.car

class PickUpTruckBuilder(CarBuilder):
    def __init__(self):
        self.car = Car(None,None,None,None,None,None,None,None)
    def set_make(self):
        self.car.make = f'Doge'
    def set_model(self):
        self.car.model = "RAM 9500"
    def set_body_type(self):
        self.car.body_type = 'Fucking TRUCK'
    def set_color(self):
        self.car.color = 'Yellow'
    def set_powertrain(self):
        self.car.powertrain = "Disell"
    def set_engine_size(self):
        self.car.engine_size = 9.6
    def set_door_count(self):
        self.car.door_count = 4
    def set_options(self):
        self.car.options = ["King Cab", "Leather interior", "Red Neck Packege (LEVEL 5000)"]
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
builder_suv = SUVBuilder()
builder_pickup = PickUpTruckBuilder()
director = Director(builder)
director_suv = Director(builder_suv)
director_pickup = Director(builder_pickup)
sports_car = director.build_car()
suv_car = director_suv.build_car()
pickup_car = director_pickup.build_car()
sports_car.show_info()
suv_car.show_info()
pickup_car.show_info()


# ================= PASTA =================

class Pasta:
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
        self.makaroni.sauce = "Кетчуп 'Торчин'"
    def add_fillings(self):
        self.makaroni.filling = "Сосиски дитячі вершкові"
    def add_toppings(self):
        self.makaroni.toppings = "Клуб сиру Вітязь"
    def show_info(self):
        return self.makaroni

class SpaghettiPastaBuilder(PastaBuilder):
    def __init__(self):
        self.makaroni = Pasta(None,None,None,None)
    def set_pasta_type(self):
        self.makaroni.pasta_type = 'Spaghetti'
    def add_sauce(self):
        self.makaroni.sauce = "Spaghetti sauce"
    def add_fillings(self):
        self.makaroni.filling = "Italian sousage with pesto"
    def add_toppings(self):
        self.makaroni.toppings = "Asiago cheese"
    def show_info(self):
        return self.makaroni

class LasagnaPastaBuilder(PastaBuilder):
    def __init__(self):
        self.makaroni = Pasta(None,None,None,None)
    def set_pasta_type(self):
        self.makaroni.pasta_type = 'Flat pasta'
    def add_sauce(self):
        self.makaroni.sauce = "Tomato sauce"
    def add_fillings(self):
        self.makaroni.filling = "ground beef"
    def add_toppings(self):
        self.makaroni.toppings = "Three cheese blend and Parmesan"
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
builder_spaghetti = SpaghettiPastaBuilder()
builder_lasagna = LasagnaPastaBuilder()
director = Director1(builder)
director_spaghetti = Director1(builder_spaghetti)
director_lasagna = Director1(builder_lasagna)
pasta = director.make_a_pasta()
spaghetti = director_spaghetti.make_a_pasta()
lasagna = director_lasagna.make_a_pasta()
pasta.show_info()
spaghetti.show_info()
lasagna.show_info()

# =====================Files==========================

class InputNumbers:
    def __init__(self,user_data):
        self.user_data = user_data
    @staticmethod
    def get_data():
        user_data = input("Enter numbers (comma/space): ")
        return user_data

class InputPath:
    def __init__(self,path):
        self.path = path
    @staticmethod
    def get_path():
        path = input("Enter path to the file: ")
        return path

class ConsolManager:
    _instance = None
    def __init__(self, target='screen', log_path=None):
        if ConsolManager._instance is not None:
            raise Exception("Only one insatnce of class")
        ConsolManager._instance = self
        self.target = target
        self.log_path = log_path
    @staticmethod
    def get_instance(target='screen', log_path=None):
        if ConsolManager._instance is None:
            ConsolManager(target, log_path)
        return ConsolManager._instance
    def log(self,msg):
        if self.target == 'file':
            if not self.log_path:
                print(msg)
                return
            with open(self.log_path,'a',encoding='utf-8') as f:
                f.write(msg + '\n')
        else:
            print(msg)

def parse_numbers(raw):
    raw = raw.replace(',', ' ')
    parts = [p.strip() for p in raw.split(' ') if p.strip()!='']
    nums = []
    for p in parts:
        try:
            nums.append(float(p))
        except ValueError:
            raise ValueError(f"Not a number: '{p}'")
    if not nums:
        raise ValueError("No numbers provided")
    return nums

def save_text(numbers, path):
    mn = min(numbers)
    mx = max(numbers)
    with open(path,'w',encoding='utf-8') as f:
        f.write("Numbers:\n")
        f.write(", ".join(f"{n:g}" for n in numbers) + "\n")
        f.write(f"Min: {mn:g}\n")
        f.write(f"Max: {mx:g}\n")
    return mn, mx

dest = input("Log to 'screen' or 'file'? ").strip().lower()
if dest == 'file':
    lp = input("Enter path to LOG file: ").strip()
    log_manager = ConsolManager.get_instance(target='file', log_path=lp)
else:
    log_manager = ConsolManager.get_instance(target='screen')
try:
    raw = InputNumbers.get_data()
    log_manager.log("[app] numbers captured")
    nums = parse_numbers(raw)
    log_manager.log(f"[app] parsed {len(nums)} numbers")
    out_path = InputPath.get_path()
    log_manager.log(f"[app] output path: {out_path}")
    mn, mx = save_text(nums, out_path)
    log_manager.log(f"[repo] wrote text to {out_path}")

    print("\n--- OUTPUT ---")
    print("Numbers:", ", ".join(f"{n:g}" for n in nums))
    print(f"Min: {mn:g}")
    print(f"Max: {mx:g}")
    log_manager.log("[app] output printed")

except Exception as e:
    print(f"Error: {e}")
    log_manager.log(f"[error] {e}")

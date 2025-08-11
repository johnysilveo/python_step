from abc import abstractmethod


class Airplane:
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,
                 engine_power,jet,t_prop,payload,passengers):
        self.make = make
        self.model = model
        self.gen = gen
        self.typo = typo
        self.role = role
        self.engine_num = engine_num
        self.engine_make = engine_make
        self.engine_power = engine_power
        self.manufactor = manufactor
        self.t_prop = t_prop
        self.passengers = passengers
        self.payload = payload
        self.jet = jet

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.role == other.role
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Airplane):
            return self.passengers + other.passengers
        elif isinstance(other, int):
            return self.passengers + other
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Airplane):
            return self.passengers - other.passengers
        elif isinstance(other, int):
            return self.passengers - other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers > other.passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers < other.passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passengers >= other.passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passengers <= other.passengers
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.passengers += other
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.passengers -= other
            return self
        return NotImplemented

    def show_info(self):
        return (f"Make: {self.make}\nModel: {self.model}\nGeneration: {self.gen}\nType: {self.typo}"
                f"\nRole: {self.role}\nNumber of engines: {self.engine_num}\nEngine make: {self.engine_make}"
                f"\nEngine power output in lbf: {self.engine_power}\nManufacture: {self.manufactor}")


class Passenger(Airplane):
    def __init__(self,make,model,gen,typo,manufactor,role,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,
                         engine_make,engine_power,jet,t_prop,payload,passengers)
        self.num_made = num_made
        self.interior_config = interior_config
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + (
            f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}"
            f"\nInterior configuration: {self.interior_config}\nPassenger capacity: {self.passengers} people\n"
            f"Max payload: {self.payload} kg")


class Cargo(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,
                         engine_make,engine_power,jet,t_prop,payload,passengers)
        self.num_made = num_made
        self.interior_config = interior_config
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + (
            f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}"
            f"\nCargo layout: {self.interior_config}\nMax payload: {self.payload} kg")


b747 = Passenger(
    make="Boeing", role="Passenger transport", model="747-400", gen="Modern", typo="Wide-body",
    manufactor="Boeing",engine_num=4, engine_make="Pratt & Whitney PW4056", engine_power="56,000 lbf each",
    interior_config="3-class (416 pax)", num_made=694, crew=2, years_of_service="1989–2023",
    jet="Yes", t_prop="No", payload=112760, passengers=416)

b737 = Passenger(
    make="Boeing", model="737-800",role="Passenger transport", gen="Modern", typo="Narrow-body",
    manufactor="Boeing",
    engine_num=2, engine_make="CFM56-7B", engine_power="27,300 lbf each",
    interior_config="2-class (189 pax)", num_made=5000, crew=2, years_of_service="1998–present",
    jet="Yes", t_prop="No", payload=20400, passengers=189)

a380 = Passenger(
    make="Airbus", model="A380-800",role="Passenger transport", gen="Modern", typo="Superjumbo",
    manufactor="Airbus",
    engine_num=4, engine_make="Rolls-Royce Trent 900", engine_power="70,000 lbf each",
    interior_config="3-class (555 pax)", num_made=251, crew=3, years_of_service="2007–2021",
    jet="Yes", t_prop="No", payload=84000, passengers=555)

trident = Passenger(
    make="Hawker Siddeley",role="Passenger transport", model="Trident 3B", gen="Early Jet Age",
    typo="Narrow-body", manufactor="Hawker Siddeley",
    engine_num=3, engine_make="Rolls-Royce Spey", engine_power="12,250 lbf each",
    interior_config="2-class (180 pax)", num_made=117, crew=3, years_of_service="1964–1986",
    jet="Yes", t_prop="No", payload=15870, passengers=180)

an225 = Cargo(
    make="Antonov",role="Cargo transport", model="An-225 Mriya", gen="Modern", typo="Heavy lift",
    manufactor="Antonov",
    engine_num=6, engine_make="Ivchenko Progress D-18T", engine_power="51,600 lbf each",
    interior_config="Open floor cargo deck", num_made=1, crew=6, years_of_service="1988–2022",
    jet="Yes", t_prop="No", payload=250000, passengers=0)

superguppy = Cargo(
    make="Aero Spacelines",role="Cargo transport", model="Super Guppy", gen="Cold War era",
    typo="Oversized cargo", manufactor="Aero Spacelines",
    engine_num=4, engine_make="Allison T56", engine_power="4,590 shp each",
    interior_config="Cargo bubble", num_made=5, crew=4, years_of_service="1965–present",
    jet="No", t_prop="Yes", payload=24000, passengers=0)

print(b747.show_info(), "\n")
print(b737.show_info(),'\n')
print(a380.show_info(),'\n')
print(trident.show_info(),'\n')
print(an225.show_info(),'\n')
print(superguppy.show_info())



class Flat:
    def __init__(self,sqf,room_num,bath_num,price):
        self.sqf = sqf
        self.room_num = room_num
        self.bath_num = bath_num
        self.price = price

    def __eq__(self, other):
        if isinstance(other,Flat):
            return self.sqf == other.sqf
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other,Flat):
            return self.sqf != other.sqf
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return (self.price > other.price and self.room_num > other.room_num
                    and self.bath_num > other.bath_num)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return (self.price < other.price and self.room_num < other.room_num
                    and self.bath_num < other.bath_num)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return (self.price >= other.price and self.room_num >= other.room_num
                    and self.bath_num >= other.bath_num)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return (self.price <= other.price and self.room_num <= other.room_num
                    and self.bath_num <= other.bath_num)
        return NotImplemented

    def show_info(self):
        return (f"price is {self.price}"
                f"sqf is {self.sqf}"
                f"number of bathrooms is {self.bath_num}"
                f"number of bedrooms is {self.room_num}")

f1 = Flat(1200, 3, 2, 300000)
f2 = Flat(1200, 4, 3, 350000)

print(f"\nf1 == f2")
print(f1 != f2)
print(f1 < f2)



class Shape:
    def __init__(self,lon,lat):
        self.lon = lon
        self.lat = lat
    @abstractmethod
    def show_info(self):
        return
    def draw(self):
        return
    @abstractmethod
    def save(self):
        return
    @abstractmethod
    def load(self):
        return

class Square(Shape):
    def __init__(self,length,height,lon,lat):
        super().__init__(lon,lat)
        self.length = length
        self.height = height

    def show_info(self):
        return (f"Length = {self.length}\n"
                f"Height = {self.height}\n"
                f"Coordinatas = {self.lon}, {self.lat}\n")

    def draw(self):
        print(' ' + '_' * self.length)
        for i in range(self.height - 2):
            print('|' + ' ' * self.length + '|')
        if self.height > 1:
            print('|' + '_' * self.length + '|')

    def save(self):
        with open('square.txt','w',encoding='utf-8') as file:
            file.write(f"Shape: Square\n")
            file.write(f"Height: {self.height}\n")
            file.write(f"Length: {self.length}\n")
            file.write(f"Coordinatas : ({self.lon},{self.lat})\n")

    def load(self):
        with open('square.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            height = int(lines[1].split(":")[1].strip())
            length = int(lines[2].split(":")[1].strip())
            coordinatas = lines[3].split(":")[1].strip()
            lon, lan = coordinatas.strip("()").split(",")
            lon = float(lon.strip())
            lan = float(lan.strip())
            return Square(length, height, lon, lan)


class Rectangle(Shape):
    def __init__(self,length,height,lon,lat):
        super().__init__(lon,lat)
        self.length = length
        self.height = height

    def show_info(self):
        return (f"Length = {self.length}\n"
                f"Height = {self.height}\n"
                f"Coordinatas = {self.lon}, {self.lat}\n")

    def draw(self):
        print(' ' + '_' * self.length)
        for i in range(self.height - 2):
            print('|' + ' ' * self.length + '|')
        if self.height > 1:
            print('|' + '_' * self.length + '|')

    def save(self):
        with open('rectangle.txt','w',encoding='utf-8') as file:
            file.write(f"Shape: Rectangle\n")
            file.write(f"Height: {self.height}\n")
            file.write(f"Length: {self.length}\n")
            file.write(f"Coordinatas : ({self.lon},{self.lat})\n")

    def load(self):
        with open('rectangle.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            height = int(lines[1].split(":")[1].strip())
            length = int(lines[2].split(":")[1].strip())
            coordinatas = lines[3].split(":")[1].strip()
            lon, lat = coordinatas.strip("()").split(",")
            lon = float(lon.strip())
            lat = float(lat.strip())
            return Rectangle(length, height, lon, lat)

class Circle(Shape):
    def __init__(self,radius,lon,lat):
        super().__init__(lon,lat)
        self.radius = radius

    def show_info(self):
        return (f"The radius of the circle is : {self.radius}\n"
                f"Coordinatas are : {self.lon}, {self.lat}\n")
#>>>>>>>>>>>>>>>>>>>>>>>>>>This draw i asked chat to create<<<<<<<<<<<<<<<<<<<
    def draw(self):
        r = self.radius
        for y in range(-r, r + 1):
            row = ""
            for x in range(-r, r + 1):
                if x**2 + y**2 <= r**2:
                    row += "*"
                else:
                    row += " "
            print(row)

    def save(self):
        with open('circle.txt','w',encoding='utf-8') as file:
            file.write(f"Shape: Circle\n")
            file.write(f"Radius: {self.radius}\n")
            file.write(f'Coordinatas: {self.lon}, {self.lat}\n')

    def load(self):
        with open('circle.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
            radius = int(lines[1].split(':')[1].strip())
            coordinatas = lines[2].split(":")[1].strip()
            lon, lat = coordinatas.strip("()").split(",")
            lon = float(lon.strip())
            lat = float(lat.strip())
            return Circle(radius,lon,lat)


class Ellipse(Shape):
    def __init__(self, length, height, lon, lat):
        super().__init__(lon, lat)  # координати верхнього лівого кута
        self.length = length
        self.height = height

    def show_info(self):
        return (f"Shape: Ellipse\n"
                f"Width: {self.length}\n"
                f"Height: {self.height}\n"
                f"Top-left corner: ({self.lon}, {self.lat})\n")

    def draw(self):
        print(" " * (self.length // 2) + "*")
        for i in range(1, self.height - 1):
            spaces_inside = self.length - 2
            print("*" + " " * spaces_inside + "*")
        if self.height > 1:
            print(" " + "*" * (self.length - 2))
    def save(self):
        with open('ellipse.txt','w',encoding='utf-8') as file:
            file.write(f"Shape: Ellipse\n")
            file.write(f"Length: {self.length}\n")
            file.write(f"Height: {self.height}\n")
            file.write(f'Coordinatas: {self.lon}, {self.lat}\n')

    def load(self):
        with open('ellipse.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
            height = int(lines[1].split(":")[1].strip())
            length = int(lines[2].split(":")[1].strip())
            coordinatas = lines[3].split(":")[1].strip()
            lon, lat = coordinatas.strip("()").split(",")
            lon = float(lon.strip())
            lat = float(lat.strip())
            return Ellipse(length,height,lon,lat)

figures = [
    Square(4, 4, 0, 0),
    Rectangle(6, 3, 2, 2),
    Circle(4, 5, 5),
    Ellipse(8, 4, 1, 1)
]

for figure in figures:
    figure.save()

loaded_figures = []
loaded_figures.append(Square(0, 0, 0, 0).load())
loaded_figures.append(Rectangle(0, 0, 0, 0).load())
loaded_figures.append(Circle(0, 0, 0).load())
loaded_figures.append(Ellipse(0, 0, 0, 0).load())

for fig in loaded_figures:
    print(fig.show_info())
    fig.draw()
    print('-' * 30)
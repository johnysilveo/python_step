class Passport:
    def __init__(self,name,surname,dob,address,country,city,maritail_status,passport_num):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.country = country
        self.maritial_status = maritail_status
        self.city = city
        self.passport_num = passport_num

    def __str__(self):
        return f"Name: {self.name} {self.surname}, DOB: {self.dob}"


class ForeignPassport(Passport):
    def __init__(self,name,surname,dob,address,country,city,maritail_status,visas,passport_num):
        super().__init__(name,surname,dob,address,country,city,maritail_status,passport_num)
        self.visas = visas
        self.passport_num = passport_num


    def show_info(self):
        return f"\n{self.name}\n{self.surname}\n{self.dob}\n{self.address}\n{self.country}\n{self.city}\n{self.maritial_status},\n{self.visas}\n{self.passport_num}"

f_pass = ForeignPassport("Johny", "Smith", "1990-05-12", "123 Main St", "Ukraine", "Kyiv", "Single", ["Germany", "USA", "Japan"],"UA123456")
print(f_pass.show_info())




# price, power efficient rating, brand, model, color,

class Device:
    def __init__(self, price, power_rating, brand, model, color):
        self.price = price
        self.power_rating = power_rating
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        return (f"Brand: {self.brand}, Model: {self.model}\n"
                f"Color: {self.color}, Power: {self.power_rating}W, Price: ${self.price}")


class CoffeeMachine(Device):
    def __init__(self, price, power_rating, brand, model, color, cup_size):
        super().__init__(price, power_rating, brand, model, color)
        self.cup_size = cup_size

    def show_info(self):
        return super().show_info() + f"\nCup Size: {self.cup_size} ml"


class MeatGrinder(Device):
    def __init__(self, price, power_rating, brand, model, color, opening_size):
        super().__init__(price, power_rating, brand, model, color)
        self.opening_size = opening_size

    def show_info(self):
        return super().show_info() + f"\nOpening Size: {self.opening_size} cm"


class Blender(Device):
    def __init__(self, price, power_rating, brand, model, color, wattage):
        super().__init__(price, power_rating, brand, model, color)
        self.wattage = wattage

    def show_info(self):
        return super().show_info() + f"\nWattage: {self.wattage} W"

c = CoffeeMachine(120, 800, "Philips", "CafeMax", "Black", 250)
b = Blender(90, 600, "Bosch", "BlendX", "Red", 1000)
m = MeatGrinder(150, 1200, "Kenwood", "GrindPro", "Silver", 5)

print(c.show_info())
print()
print(b.show_info())
print()
print(m.show_info())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Вибачте. Я зробив про літаки<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# make, model, type, pay_load, role, engine_num, engine_make, engine_power, gen

class Airplane:
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,jet,t_prop,payload,passengers):
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


    def show_info(self):
        return (f"Make: {self.make}\nModel: {self.model}\nGeneration: {self.gen}\nType: {self.typo}"
                f"\nRole: {self.role}\nNumber of engines: {self.engine_num}\nEngine make: {self.engine_make}"
                f"\nEngine power output in lbf: {self.engine_power}\nManufacture: {self.manufactor}")

class Fighter(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,stealth_level,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,jet,t_prop,payload,passengers)
        self.stealth_level = stealth_level
        self.num_made = num_made
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}\nStealth level: {self.stealth_level}"

class Attacker(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,stealth_level,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,jet,t_prop,payload,passengers)
        self.stealth_level = stealth_level
        self.num_made = num_made
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}\nStealth level: {self.stealth_level}"


class Multirole(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,stealth_level,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,jet,t_prop,payload,passengers)
        self.stealth_level = stealth_level
        self.num_made = num_made
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}\nStealth level: {self.stealth_level}"


class Bomber(Airplane):
    def __init__(self,make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,stealth_level,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,role,manufactor,engine_num,engine_make,engine_power,jet,t_prop,payload,passengers)
        self.stealth_level = stealth_level
        self.num_made = num_made
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}\nStealth level: {self.stealth_level}"

class Passenger(Airplane):
    def __init__(self,make,model,gen,typo,manufactor,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,"Passenger transport",manufactor,engine_num,
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
    def __init__(self,make,model,gen,typo,manufactor,engine_num,engine_make,engine_power,
                 interior_config,num_made,crew,years_of_service,jet,t_prop,payload,passengers):
        super().__init__(make,model,gen,typo,"Cargo transport",manufactor,engine_num,
                         engine_make,engine_power,jet,t_prop,payload,passengers)
        self.num_made = num_made
        self.interior_config = interior_config
        self.crew = crew
        self.years_of_service = years_of_service

    def show_info(self):
        return super().show_info() + (
            f"\nNumber produced: {self.num_made}\nCrew: {self.crew}\nYears in service: {self.years_of_service}"
            f"\nCargo layout: {self.interior_config}\nMax payload: {self.payload} kg")


b2 = Bomber(
    make="Northrop Grumman", model="B-2 Spirit", gen="5th", typo="Bomber", role="Stealth strategic bomber",
    manufactor="Northrop", engine_num=4, engine_make="General Electric F118", engine_power="17,300 lbf each",
    stealth_level="Very High", num_made=21, crew=2, years_of_service="1997–present",
    jet="Yes", t_prop="No", payload=23000, passengers=2)

f22 = Attacker(
    make="Lockheed Martin", model="F-22 Raptor", gen="5th", typo="Fighter", role="Air superiority",
    manufactor="Lockheed Martin", engine_num=2, engine_make="Pratt & Whitney F119", engine_power="35,000 lbf each",
    stealth_level="High", num_made=195, crew=1, years_of_service="2005–present",
    jet="Yes", t_prop="No", payload=8200, passengers=1)

a10 = Multirole(
    make="Fairchild Republic", model="A-10 Thunderbolt II", gen="3rd", typo="Attack", role="Close air support",
    manufactor="Fairchild", engine_num=2, engine_make="General Electric TF34", engine_power="9,065 lbf each",
    stealth_level="None", num_made=716, crew=1, years_of_service="1977–present",
    jet="Yes", t_prop="No", payload=7200, passengers=1)

rafale = Multirole(
    make="Dassault", model="Rafale", gen="4.5th", typo="Multirole", role="Omnirole fighter",
    manufactor="Dassault Aviation", engine_num=2, engine_make="Snecma M88", engine_power="17,000 lbf each",
    stealth_level="Medium", num_made=240, crew=1, years_of_service="2001–present",
    jet="Yes", t_prop="No", payload=9500, passengers=1)

b747 = Passenger(
    make="Boeing", model="747-400", gen="Modern", typo="Wide-body", manufactor="Boeing",
    engine_num=4, engine_make="Pratt & Whitney PW4056", engine_power="56,000 lbf each",
    interior_config="3-class (416 pax)", num_made=694, crew=2, years_of_service="1989–2023",
    jet="Yes", t_prop="No", payload=112760, passengers=416)

b737 = Passenger(
    make="Boeing", model="737-800", gen="Modern", typo="Narrow-body", manufactor="Boeing",
    engine_num=2, engine_make="CFM56-7B", engine_power="27,300 lbf each",
    interior_config="2-class (189 pax)", num_made=5000, crew=2, years_of_service="1998–present",
    jet="Yes", t_prop="No", payload=20400, passengers=189)

a380 = Passenger(
    make="Airbus", model="A380-800", gen="Modern", typo="Superjumbo", manufactor="Airbus",
    engine_num=4, engine_make="Rolls-Royce Trent 900", engine_power="70,000 lbf each",
    interior_config="3-class (555 pax)", num_made=251, crew=3, years_of_service="2007–2021",
    jet="Yes", t_prop="No", payload=84000, passengers=555)

trident = Passenger(
    make="Hawker Siddeley", model="Trident 3B", gen="Early Jet Age", typo="Narrow-body", manufactor="Hawker Siddeley",
    engine_num=3, engine_make="Rolls-Royce Spey", engine_power="12,250 lbf each",
    interior_config="2-class (180 pax)", num_made=117, crew=3, years_of_service="1964–1986",
    jet="Yes", t_prop="No", payload=15870, passengers=180)

an225 = Cargo(
    make="Antonov", model="An-225 Mriya", gen="Modern", typo="Heavy lift", manufactor="Antonov",
    engine_num=6, engine_make="Ivchenko Progress D-18T", engine_power="51,600 lbf each",
    interior_config="Open floor cargo deck", num_made=1, crew=6, years_of_service="1988–2022",
    jet="Yes", t_prop="No", payload=250000, passengers=0)

superguppy = Cargo(
    make="Aero Spacelines", model="Super Guppy", gen="Cold War era", typo="Oversized cargo", manufactor="Aero Spacelines",
    engine_num=4, engine_make="Allison T56", engine_power="4,590 shp each",
    interior_config="Cargo bubble", num_made=5, crew=4, years_of_service="1965–present",
    jet="No", t_prop="Yes", payload=24000, passengers=0)

print(b2.show_info(), "\n")
print(f22.show_info(), "\n")
print(a10.show_info(), "\n")
print(rafale.show_info(),'\n')
print(b747.show_info(), "\n")
print(b737.show_info(),'\n')
print(a380.show_info(),'\n')
print(trident.show_info(),'\n')
print(an225.show_info(),'\n')
print(superguppy.show_info())





class Money:
    def __init__(self, whole_dollars, cents):
        self.whole_dollars = whole_dollars
        self.cents = cents

    def change_info(self):
        new_wd = int(input("Enter new $: "))
        new_c = int(input("Enter new cents: "))
        self.whole_dollars = new_wd
        self.cents = new_c

    def show_info(self):
        return f"Price is {self.whole_dollars}$ and {self.cents} cents."

    def decrease(self, amount_dollars, amount_cents):
        total_cents = self.whole_dollars * 100 + self.cents
        decrease_cents = amount_dollars * 100 + amount_cents
        new_total = max(total_cents - decrease_cents, 0)
        self.whole_dollars = new_total // 100
        self.cents = new_total % 100


class Product(Money):
    def __init__(self, whole_dollars, cents, make, model):
        super().__init__(whole_dollars, cents)
        self.make = make
        self.model = model

    def show_info(self):
        return (f"Product: {self.make} {self.model}\n" +
                super().show_info())

    def decrease_price(self, amount_dollars, amount_cents):
        self.decrease(amount_dollars, amount_cents)





class TempConverter:

    conversion_count = 0

    @staticmethod
    def c_to_f(cel):
        TempConverter.conversion_count += 1
        far = (cel*9/5) + 32
        return far

    @staticmethod
    def f_to_c(far):
        TempConverter.conversion_count += 1
        cel = (far -32) * 5/9
        return cel

    @staticmethod
    def get_conversion_count():
        return TempConverter.conversion_count

print(TempConverter.c_to_f(0))      # 32.0
print(TempConverter.f_to_c(98.6))   # 37.0
print(TempConverter.get_conversion_count())  # 2




#f-sm, m-inch, inch-m, sm-f, m-y, y-m, mil-km, km-mil

class ConverterImperialToMetric:

    @staticmethod
    def foot_to_sm(foot):
        sm = foot *30.48
        return sm
    @staticmethod
    def sm_to_foot(sm):
        foot = sm/30.48
        return foot
    @staticmethod
    def meter_to_inch(meter):
        inch = meter/0.0254
        return inch
    @staticmethod
    def inch_to_meter(inch):
        meter = inch * 0.0254
        return meter
    @staticmethod
    def meter_to_yard(meter):
        yard = meter * 1.0936133
        return yard
    @staticmethod
    def yard_to_meter(yard):
        meter = yard/1.0936133
        return meter
    @staticmethod
    def km_to_mil(km):
        mil = km * 0.621371
        return mil
    @staticmethod
    def mil_to_km(mil):
        km = mil/0.621371
        return km
    @staticmethod
    def lb_to_kilo(lb):
        kilo = lb*0.45359237
        return kilo
    @staticmethod
    def kilo_to_lb(kilo):
        lb = kilo/0.45359237
        return lb
    @staticmethod
    def gal_to_litr(gal):
        litr = gal * 3.78541
        return litr
    @staticmethod
    def litr_to_gal(litr):
        gal = litr/3.78541
        return gal


feet = 6
cm = ConverterImperialToMetric.foot_to_sm(feet)
print(f"{feet} feet = {cm:.2f} cm")

cm = 180
feet = ConverterImperialToMetric.sm_to_foot(cm)
print(f"{cm} cm = {feet:.2f} feet")

meters = 2
inches = ConverterImperialToMetric.meter_to_inch(meters)
print(f"{meters} meters = {inches:.2f} inches")

inches = 50
meters = ConverterImperialToMetric.inch_to_meter(inches)
print(f"{inches} inches = {meters:.2f} meters")

km = 5
miles = ConverterImperialToMetric.km_to_mil(km)
print(f"{km} km = {miles:.2f} miles")

miles = 3.1
km = ConverterImperialToMetric.mil_to_km(miles)
print(f"{miles} miles = {km:.2f} km")

pounds = 150
kg = ConverterImperialToMetric.lb_to_kilo(pounds)
print(f"{pounds} lbs = {kg:.2f} kg")

kg = 70
pounds = ConverterImperialToMetric.kilo_to_lb(kg)
print(f"{kg} kg = {pounds:.2f} lbs")

gal = 1
liters = ConverterImperialToMetric.gal_to_litr(gal)
print(f"{gal} gallon = {liters:.2f} liters")

liters = 3.78
gal = ConverterImperialToMetric.litr_to_gal(liters)
print(f"{liters} liters = {gal:.2f} gallons")















    # def __init__(self,cel,far):
    #     self.cel = cel
    #     self.far = far
    #
    # def data_input_c(self):
    #     self.cel = input("enter temp in C: ")
    #
    # def data_input_f(self):
    #     self.far = input("enter temp in F: ")
    #
    # def c_to_f(self):
    #     self.far = (self.cel*9/5) + 32
    #
    # def f_to_c(self):
    #     self.cel = (self.far -32) * 5/9



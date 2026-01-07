# python -m venv venv

# OOP Asoslari
# a = 6
# def add():
#     pass
# print(type(a))
# print(type(add()))

class Car:
    brand = "GM"

    def __init__(self, year, price, color):
        self.year = year
        self.price = price
        self.color = color

    def __str__(self):
        return f"{self.year}-yilgi mashina"
    
    def __repr__(self):
        return f"Car(year={self.year}, price = {self.price})"
    
obj1 = Car(year=2025, price=10000, color="oq")
obj2 = Car(year=2022, price=8000, color="qizil")
obj3 = Car(year=2000, price=1000, color="qora")
# list()
# print(repr(obj1))
# print(repr(obj1))
# print(obj2.year)
# print(obj2.price)
# print(obj2.color)

# class Student:
#     def __init__(self):
#         pass

#     @staticmethod
#     def save(self, name):
#         pass

# std = Student()
# std.save()

class Car:
    brand = "GM"

    def __init__(self, year, price, color, fuel):
        self.year = year
        self.price = price
        self.color = color
        self.fuel = fuel
        self.is_engine_on = False

    def __str__(self):
        return f"{self.year}-yilgi mashina"
    
    def __repr__(self):
        return f"Car(year={self.year}, price = {self.price})"
    
    def star_car(self):
        if not self.is_engine_on:
            self.is_engine_on = True

            return f"Car is successfully turned on!"
        return f"car is already on you stupid!"
    
    def drive(self):
        if self.is_engine_on:
            return f"we are driving look at on your road!"
        return f"you should start engine on first!"
    
    def drive_to_home(self, length):
        if self.fuel > length // 10:
            return f"we are going to your home!"
        return f"please add more fuel, we can't go futher"
    
    def add_fuel(self, fuel_amount):
        self.fuel+=fuel_amount
        return self.fuel
        
gentra = Car(price=10000, color="qora", year=2023, fuel=10)
print(gentra.drive_to_home(200))
print(gentra.add_fuel(20))
print(gentra.drive_to_home(200))
# print(gentra.drive())
# print(gentra.star_car())
# print(gentra.star_car())
# print(gentra.star_car())
# print(gentra.drive())
# print(gentra.drive())

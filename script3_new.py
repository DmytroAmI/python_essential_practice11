"""
Liskov Substitution Principle
Підтипи повинні бути замінними для своїх базових типів
Класи нащадки повинні відповідати інтерфейсам класів батьків
"""
from abc import ABC, abstractmethod


class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Refuel(ABC):
    @abstractmethod
    def refuel(self):
        pass


class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'{self.make} {self.model}'


class Car(Vehicle, Drivable, Refuel):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def refuel(self):
        return f'{self} make: {self.make} is gasoline'


class HybridCar(Vehicle, Drivable, Refuel, Chargeable):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def refuel(self):
        return f'{self} make: {self.make} is gasoline'

    def charge(self):
        return f'{self} make: {self.make} is AC motor'


class ElectricCar(Vehicle, Drivable, Chargeable):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def charge(self):
        return f'{self} make: {self.make} is AC motor'


class Motorcycle(Vehicle, Drivable, Refuel):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def refuel(self):
        return f'{self} make: {self.make} is gasoline'


car = Car('Ford', 'Fiesta')
print(car.drive())
print(car.refuel())

car1 = HybridCar('Ford', 'Hybrid')
print(car1.drive())
print(car1.refuel())
print(car1.charge())

"""
Liskov Substitution Principle
Підтипи повинні бути замінними для своїх базових типів
Класи нащадки повинні відповідати інтерфейсам класів батьків
"""


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        pass

    def refuel(self):
        pass


class Car(Vehicle):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def refuel(self):
        return f'{self} make: {self.make} is gasoline'


class Motorcycle(Vehicle):
    def drive(self):
        return f'{self} make: {self.make} is drive'

    def refuel(self):
        return f'{self} make: {self.make} is gasoline'


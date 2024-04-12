"""
Dependency Inversion Principle
Абстракції не повинні залежати від деталей
Деталі мають залежати від абстракцій
"""
from abc import ABC, abstractmethod


class Switch:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        return self.device.power_on()

    def turn_off(self):
        return self.device.power_off()


class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class TV:
    def power_on(self):
        return "TV is on {}".format(self)

    def power_off(self):
        return "TV is off {}".format(self)


class Radio:
    def power_on(self):
        return "Radio is on {}".format(self)

    def power_off(self):
        return "Radio is off {}".format(self)

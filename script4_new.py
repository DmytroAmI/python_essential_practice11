"""
Interface Segregation Principle
Клієнти не повинні залежати від інтерфейсів
які вони не використовують
"""


class Powerable:
    def power_on(self):
        pass

    def power_off(self):
        pass


class VolumeControlable:
    def volume_up(self):
        pass

    def volume_down(self):
        pass


class TV(Powerable, VolumeControlable):
    def power_on(self):
        return "TV power on"

    def power_off(self):
        return "TV power off"

    def volume_up(self):
        return "TV volume up"

    def volume_down(self):
        return "TV volume down"


class Radio(Powerable):
    def power_on(self):
        return "Radio power on"

    def power_off(self):
        return "Radio power off"

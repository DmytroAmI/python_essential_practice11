"""
Interface Segregation Principle
Клієнти не повинні залежати від інтерфейсів
які вони не використовують
"""


class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass


class TV(Device):
    def power_on(self):
        return "TV power on"

    def power_off(self):
        return "TV power off"

    def volume_up(self):
        return "TV volume up"

    def volume_down(self):
        return "TV volume down"


class Radio(Device):
    def power_on(self):
        return "Radio power on"

    def power_off(self):
        return "Radio power off"

    def volume_up(self):
        return "Radio power up"

    def volume_down(self):
        return "Radio power down"


tv = TV()
print(tv.power_on())
print(tv.volume_up())

radio = Radio()
print(radio.power_on())

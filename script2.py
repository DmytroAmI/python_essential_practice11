"""
Open-Closed Principle
Програмні функції мають бути відкриті для розширення,
але закриті для модифікації
Не чіпаємо існуючий код
"""


class Delivery:
    def calculate_cost(self, weight):
        pass


class StandardDelivery(Delivery):
    def calculate_cost(self, weight):
        return weight * 5


class ExpressDelivery(Delivery):
    def calculate_cost(self, weight):
        return weight * 5 + 25


class OverNightDelivery(Delivery):
    def calculate_cost(self, weight):
        return weight * 5 + 50


class DeliveryFactory:
    """Pattern Factory"""
    @staticmethod
    def create_delivery(delivery_type):
        if delivery_type == "standard":
            return StandardDelivery()
        elif delivery_type == "express":
            return ExpressDelivery()
        elif delivery_type == "overnight":
            return OverNightDelivery()


delivery = DeliveryFactory.create_delivery("standard")
print(delivery.calculate_cost(10))

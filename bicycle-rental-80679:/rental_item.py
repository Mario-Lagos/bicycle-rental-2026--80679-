from abc import ABC, abstractmethod

class RentalItem(ABC):
    def __init__(self, item_id, rental_price):
        self.item_id = item_id
        self.rental_price = rental_price
    @abstractmethod
    def rent(self):
        pass
    @abstractmethod
    def return_item(self):
        pass
    @abstractmethod
    def calculate_rental_cost(self, hours):
        pass

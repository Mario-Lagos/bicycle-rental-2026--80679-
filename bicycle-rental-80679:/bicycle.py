
from math import isfinite
from rental_item import RentalItem


class Bicycle(RentalItem):

    def __init__(self, item_id, bicycle_type, rental_price):
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("Bicycle ID cannot be empty.")

        if not isinstance(bicycle_type, str) or not bicycle_type.strip():
            raise ValueError("Bicycle type cannot be empty.")

        self._validate_price(rental_price)

        super().__init__(item_id.strip(), rental_price)

        self.bicycle_type = bicycle_type.strip()
        self.is_available = True

    @staticmethod
    def _validate_price(price):
        if (
            isinstance(price, bool)
            or not isinstance(price, (int, float))
            or not isfinite(price)
            or price < 0
        ):
            raise ValueError("Rental price must be a valid non-negative number.")

    def rent(self):
        if not self.is_available:
            raise RuntimeError("This bicycle is already rented.")

        self.is_available = False
        return True

    def return_item(self):
        if self.is_available:
            raise RuntimeError("This bicycle has not been rented.")

        self.is_available = True
        return True

    def set_rental_price(self, new_price):
        self._validate_price(new_price)
        self.rental_price = new_price

    def calculate_rental_cost(self, hours):
        if (
            isinstance(hours, bool)
            or not isinstance(hours, (int, float))
            or not isfinite(hours)
            or hours <= 0
        ):
            raise ValueError("Rental hours must be a positive number.")

        return self.rental_price * hours

    @classmethod
    def create_standard_bicycle(cls, item_id, bicycle_type):
        return cls(item_id, bicycle_type, 10.0)

    def __str__(self):
        status = "Available" if self.is_available else "Rented"

        return (
            f"Bicycle ID: {self.item_id}, "
            f"Type: {self.bicycle_type}, "
            f"Price per hour: €{self.rental_price:.2f}, "
            f"Status: {status}"
        )




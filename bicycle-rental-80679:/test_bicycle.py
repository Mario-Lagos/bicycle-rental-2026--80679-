
import unittest

from bicycle import Bicycle
from rental_item import RentalItem


class TestBicycle(unittest.TestCase):

    def setUp(self):
        self.bike = Bicycle("B001", "Mountain Bike", 10.0)

    def test_create_bicycle(self):
        self.assertEqual(self.bike.item_id, "B001")

    def test_initial_availability(self):
        self.assertTrue(self.bike.is_available)

    def test_rent_bicycle(self):
        self.bike.rent()
        self.assertFalse(self.bike.is_available)

    def test_rent_already_rented_bicycle(self):
        self.bike.rent()

        with self.assertRaises(RuntimeError):
            self.bike.rent()

    def test_return_bicycle(self):
        self.bike.rent()
        self.bike.return_item()
        self.assertTrue(self.bike.is_available)

    def test_return_available_bicycle(self):
        with self.assertRaises(RuntimeError):
            self.bike.return_item()

    def test_calculate_rental_cost(self):
        cost = self.bike.calculate_rental_cost(3)
        self.assertEqual(cost, 30.0)

    def test_change_rental_price(self):
        self.bike.set_rental_price(15.0)
        self.assertEqual(self.bike.rental_price, 15.0)

    def test_reject_negative_price(self):
        with self.assertRaises(ValueError):
            self.bike.set_rental_price(-5)

    def test_reject_zero_rental_hours(self):
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(0)

    def test_alternative_constructor(self):
        bike = Bicycle.create_standard_bicycle(
            "B002", "City Bike"
        )
        self.assertEqual(bike.rental_price, 10.0)

    def test_rental_item_is_abstract(self):
        with self.assertRaises(TypeError):
            RentalItem("R001", 10.0)


if __name__ == "__main__":
    unittest.main()

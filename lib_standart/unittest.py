import unittest
from rental_unittest import RentalByHour
from rental_unittest import RentalByDay
from rental_unittest import RentalByWeek
from rental_unittest import FamilyRental


class TestRentalByHour(unittest.TestCase):

    def test_rental_by_hour(self):
        self.assertAlmostEqual(RentalByHour(1).rental_by_hour(), 5)

    def test_rental_hour_values(self):
        self.assertRaises(ValueError, RentalByHour, -5)

    def test_rental_hour_type(self):
        self.assertRaises(TypeError, RentalByHour, True)
        self.assertRaises(TypeError, RentalByHour, 2 + 3j)
        self.assertRaises(TypeError, RentalByHour, "string")


class TestRentalByDay(unittest.TestCase):

    def test_rental_by_day(self):
        self.assertAlmostEqual(RentalByDay(1).rental_by_day(), 20)

    def test_rental_day_values(self):
        self.assertRaises(ValueError, RentalByDay, -5)

    def test_rental_day_type(self):
        self.assertRaises(TypeError, RentalByDay, True)
        self.assertRaises(TypeError, RentalByDay, 2 + 3j)
        self.assertRaises(TypeError, RentalByDay, "string")


class TestRentalByWeek(unittest.TestCase):

    def test_rental_by_week(self):
        self.assertAlmostEqual(RentalByWeek(1).rental_by_week(), 60)

    def test_rental_week_values(self):
        self.assertRaises(ValueError, RentalByWeek, -5)

    def test_rental_week_type(self):
        self.assertRaises(TypeError, RentalByWeek, True)
        self.assertRaises(TypeError, RentalByWeek, 2 + 3j)
        self.assertRaises(TypeError, RentalByWeek, "string")


class TestFamilyRental(unittest.TestCase):

    def test_family_rental_values(self):
        self.assertRaises(ValueError, FamilyRental, -5)

    def test_family_rental_type(self):
        self.assertRaises(TypeError, FamilyRental, True)
        self.assertRaises(TypeError, FamilyRental, 2 + 3j)
        self.assertRaises(TypeError, FamilyRental, "string")

#Ejecutar test con el siguiente comando:
#python3 -m unittest test_rental.py
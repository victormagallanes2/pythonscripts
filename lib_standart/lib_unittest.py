import unittest
# from rental_unittest import RentalByHour
# from rental_unittest import RentalByDay
# from rental_unittest import RentalByWeek
# from rental_unittest import FamilyRental


# class RentalByHour(object):

#     def __init__(self, hour):
#         self.hour = hour

#         if type(self.hour) not in [int, float]:
#             raise TypeError("the hour must be non-negative real number")

#         if self.hour < 0:
#             raise ValueError("The hour cannot be negative")

#     def rental_by_hour(self):
#         price = 5
#         total = price * self.hour
#         return total


# class RentalByDay(object):

#     def __init__(self, day):
#         self.day = day

#         if type(self.day) not in [int, float]:
#             raise TypeError("the day must be non-negative real number")

#         if self.day < 0:
#             raise ValueError("The day cannot be negative")

#     def rental_by_day(self):
#         price = 20
#         total = price * self.day
#         return total


# class RentalByWeek(object):

#     def __init__(self, week):
#         self.week = week

#         if type(self.week) not in [int, float]:
#             raise TypeError("the week must be non-negative real number")

#         if self.week < 0:
#             raise ValueError("The week cannot be negative")

#     def rental_by_week(self):
#         price = 60
#         total = price * self.week
#         return total


# class FamilyRental(object):

#     def __init__(self, quantity_rental):
#         self.quantity_rental = quantity_rental

#         if type(self.quantity_rental) not in [int, float]:
#             raise TypeError("the quantity rental must be non-negative real number")

#         if self.quantity_rental < 0:
#             raise ValueError("The quantity rental cannot be negative")

#     def family_rental(self):
#         z = 1
#         total = 0
#         while z <= self.quantity_rental:
#             z += 1
#             tipo = int(input("Enter type of rental: "))
#             if tipo == 1:
#                 hour = int(input("How many hours will you rent?: "))
#                 total = RentalByHour(hour).rental_by_hour() + total

#             elif tipo == 2:
#                 day = int(input("How many days will you rent?: "))
#                 total = RentalByDay(day).rental_by_day() + total

#             elif tipo == 3:
#                 week = int(input("How many weeks will you rent?: "))
#                 total = RentalByWeek(week).rental_by_week() + total

#             elif tipo == 4:
#                 break
#             else:
#                 input("You have not pressed any correct option...")
#         print("you must pay:")
#         total -= (total * 0.30)
#         return total

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


class RentalByHour(object):

    def __init__(self, hour):
        self.hour = hour

        if type(self.hour) not in [int, float]:
            raise TypeError("the hour must be non-negative real number")

        if self.hour < 0:
            raise ValueError("The hour cannot be negative")

    def rental_by_hour(self):
        price = 5
        total = price * self.hour
        return total


class RentalByDay(object):

    def __init__(self, day):
        self.day = day

        if type(self.day) not in [int, float]:
            raise TypeError("the day must be non-negative real number")

        if self.day < 0:
            raise ValueError("The day cannot be negative")

    def rental_by_day(self):
        price = 20
        total = price * self.day
        return total


class RentalByWeek(object):

    def __init__(self, week):
        self.week = week

        if type(self.week) not in [int, float]:
            raise TypeError("the week must be non-negative real number")

        if self.week < 0:
            raise ValueError("The week cannot be negative")

    def rental_by_week(self):
        price = 60
        total = price * self.week
        return total


class FamilyRental(object):

    def __init__(self, quantity_rental):
        self.quantity_rental = quantity_rental

        if type(self.quantity_rental) not in [int, float]:
            raise TypeError("the quantity rental must be non-negative real number")

        if self.quantity_rental < 0:
            raise ValueError("The quantity rental cannot be negative")

    def family_rental(self):
        z = 1
        total = 0
        while z <= self.quantity_rental:
            z += 1
            tipo = int(input("Enter type of rental: "))
            if tipo == 1:
                hour = int(input("How many hours will you rent?: "))
                total = RentalByHour(hour).rental_by_hour() + total

            elif tipo == 2:
                day = int(input("How many days will you rent?: "))
                total = RentalByDay(day).rental_by_day() + total

            elif tipo == 3:
                week = int(input("How many weeks will you rent?: "))
                total = RentalByWeek(week).rental_by_week() + total

            elif tipo == 4:
                break
            else:
                input("You have not pressed any correct option...")
        print("you must pay:")
        total -= (total * 0.30)
        return total
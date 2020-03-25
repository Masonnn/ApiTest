class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print('too much')
#
#
# my_car = Car('audi', 'a4', 2020)
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)
#
# my_car.fill_tank()
# print(my_car.fuel_level)
# my_car.drive()
#
# my_truck = Car('Toyota', 'Tacoma', 2010)
#
# my_car.fuel_level = 5
# print(my_car.fuel_level)
#
# my_car.update_fuel_level(15)
# print(my_car.fuel_level)
#

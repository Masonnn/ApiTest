from cheatSheet.Battery import Battery
from cheatSheet.Car import Car


class ElecCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # self.battery_size = 70
        # self.charge_level = 0
        self.battery = Battery()

    def charge(self):
        self.battery.charge_level = 100
        print('fully charged')


my_ecar = ElecCar('tesla', 'Model s', 2006)

my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()

from cheatSheet.Car import Car
from cheatSheet.ElecCar import ElecCar

gas_fleet = []
e_fleet = []

for _ in range(500):
    car = Car('ford', 'Focus', 2019)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElecCar('Nissan', 'leaf', 2016)
    e_fleet.append(ecar)

for car in gas_fleet:
    car.fill_tank()
for ecar in e_fleet:
    ecar.charge()

print('Gas cars: ', len(gas_fleet))
print('Electric cars: ', len(e_fleet))

from chap09 import Car as c
from car import Battery,ElectricCar
import numpy as np

my_new_car = c('audi','a4',2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.update_odometer(20)
my_new_car.increment_odometer(20)

my_new_car.read_odometer()


my_battery = Battery()
my_battery.describe_battery()

my_electric_car = ElectricCar('nissan','leaf',2024)
my_electric_car.battery
print("전기차는 {}-kWh".format(my_electric_car.battery.battery_size))





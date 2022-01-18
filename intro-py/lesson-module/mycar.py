from car import Car

mycar = Car('audi', 'R4', 2021)
print(mycar.get_descriptive_name())

mycar.odometer_reading = 240
mycar.read_odometer()
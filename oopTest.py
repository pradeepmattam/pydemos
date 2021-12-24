from car import Car

car_1 = Car('Honda', 'CRV', 2014)
car_2 = Car('Honda', 'Accord', 2017)
car_1.drive().stop()

print('car_1 has '+str(car_1.wheels)+" wheels")

car_2.drive().stop()
print('car_2 has '+str(car_2.wheels)+" wheels")

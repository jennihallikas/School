import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current = 0
        self.distance = 0

    def accelerate(self, acceleration):
        self.current = min(max(self.current + acceleration, 0), self.max_speed)
        #speed = self.current + acceleration
        #if self.max_speed > speed and speed > 0:
            #self.current += acceleration
        #elif speed < 0:
            #self.current = 0
        #else:
            #pass

    def drive(self, hours):
        self.distance += self.current*hours

    def __int__(self, current):
        self.current = current



ferrari = Car("ABC", 142)
print(f"{ferrari.reg_num}, {ferrari.max_speed}")

ferrari.accelerate(+30)
ferrari.accelerate(+70)
ferrari.accelerate(+50)
#print(f"Current speed is {ferrari.current}")
ferrari.accelerate(-200)
print(f"Current speed is {ferrari.current}")

ferrari.accelerate(60)
ferrari.drive(1.5)
print(f"{ferrari.distance}")


carList = []
for i in range(10):
    carList.append(Car("ABC-" + str(i+1), random.randint(100, 200)))

distance = 0
while distance < 10000:
    for car in carList:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        distance = max(car.distance, distance)


for car in carList:
    print(f"{car.reg_num}, {car.max_speed}km/h, {car.distance}km")

# 4 ex.10
class Race:
    def __init__(self, name, km, car_list):
        self.name = name
        self.km = km
        self.car_list = car_list

    def hour_passes(self):
        for c in self.car_list:
            c.accelerate(random.randint(-10, 15))
            c.drive(1)


    def print_status(self):
        print(self.name + ":")
        for c in self.car_list:
            print(f"{c.reg_num:6s}: {c.current:3d}, {c.distance} km")
        return self.car_list


    def race_finished(self):
        for c in self.car_list:
            if c.distance < self.km:
                return False
        return True

car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i+1), random.randint(0,100)))


race = Race("Grand Demolition Derby", 8000, car_list)
n = 0


for i in range(10):
    n += 1
    print(i)
    if race.race_finished():
        break
    race.hour_passes()

    if i%10 == 0:
        print(race)

print(f"The final result after {n} hours is:")
race.print_status()
# ex.11, 2
class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, capacity):
        self.capacity = capacity
        super().__init__(reg_num, max_speed)

    def print_information(self):
        print(f"The electric car with reg number {self.reg_num} has travelled {self.distance} km, current speed is {self.current} and capacity of battery is {self.capacity}")

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, volume):
        self.volume = volume
        super().__init__(reg_num, max_speed)

    def print_information(self):
        print(f"The gasoline car with a reg num {self.reg_num} has travelled {self.distance} km, current speed is {self.current} and it has {self.volume} liters")


e = ElectricCar("EFK-12", 111, 70)
g = GasolineCar("HHH-12", 222, 64)

e.current = 200
g.current = 152

e.drive(3)
g.drive(3)

e.print_information()
g.print_information()
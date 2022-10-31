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


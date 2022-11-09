class Elevator:
  def __init__(self):
      self.floor = 0

  def floor_up(self):
      self.floor += 1

  def floor_down(self):
      self.floor -= 1

  def go_to_floor(self, f):
      while 1:
          if self.floor > f:
              self.floor_down()
          elif self.floor < f:
              self.floor_up()
          else:
              break

h = Elevator()

h.go_to_floor(5)
print(h.floor)
print(f"The elevator is going to {h.floor}th floor")
h.go_to_floor(0)
print(h.floor)
print(f"The elevator is going to {h.floor} floor")

# 2, 3
class Building:
    def __init__(self, top_floor, bottom_floor, elevator_list):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator())

    def run_elevator(self, number, f):
        print(f"The elevator number {number} is running")
        self.elevator_list[number - 1].go_to_floor(f)

    def fire_alarm(self):
        for i in self.elevator_list:
            i.go_to_floor(0)


b = Building(10, 1, 3)

b.run_elevator(1, 3)
b.run_elevator(2, 4)
b.run_elevator(3, 1)

b.fire_alarm()




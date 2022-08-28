 phase 1
import math
import random

name = input("What is your name? ")
print("Hello, " + name + "!")

 phase 2
radius = float(input("Give the radius? "))
print(f"Area is {math.pi * radius ** 2:10.1f}")

 phase 6
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

lenght = float(input("Give me the lenght? "))
width = float(input("Give me the width? "))
perimeter = lenght * 2 + width * 2
area = lenght * width
print("Perimeter is " + str(perimeter))
print("Area is " + str(area))

number = int(input("Give me a number"))
number2 = int(input("Give me a number"))
number3 = int(input("Give me a number"))
sum = number + number2 + number3
product = number * number2 * number3
average = (number + number2 + number3)/3
print("sum: " + str(sum))
print("average: " + str(average))
print("product: " + str(product))

T = float(input("Give me a talent"))
P = float(input("Give me a pound"))
L = float(input("Give me a lot"))

print("Enter weight in medieval talents, pounds and lots")
T = float(input("Enter talents: "))
P = float(input("Enter pounds: ")
L = float(input("Enter lots: "))
print("The weights in modern units are: ")
weight_gramms = T*20*32*13.3+P*32*13+L*13.3
weight_kilos = int(weight_gramms/1000)

print(weight_kilos)

weight_gramms_left = weight_gramms-weight_kilos*1000

print(f"The weight in modern units is: {weight_kilos} kg and {weight_gramms_left: .2f} gramms")






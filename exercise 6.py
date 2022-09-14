# 1 Dice
import math
import random


def dice():
    return random.randint(1,6)
number = dice()
while number != 6:
    print(number)
    number = dice()
print(number)

x = int(input("How many sides the dice has?"))
def diceRoll():
    return random.randint(1, x)

number = diceRoll()
while int(number) < x:
    print(number)

    number = diceRoll()
print(number)
# 3


def gasoline(gallons):
    return gallons * 3.785


litres = float(input("Input gallons: "))
while litres >= 0:
    litres = float(input("Input gallons or a negative value to exit: "))
    print(f"This amount is {gasoline(litres):.3f} litres")


# 4
def list(listInt):
    listSum = 0
    for i in listInt:
        listSum += i
    return listSum


listFinal = [6, 9, 4, 2, 3, 1, 5, 2]
print("The sum of the list is:", list(listFinal))

# 5
def removeOdd(i):
    return [x for x in i if x % 2 == 0]


listFirst = [1, 5, 4, 9, 6, 7]
print("First list with numbers is:", listFirst)
print("Second list with even numbers is:", removeOdd(listFirst))

# 6
def pizza(diameter, price):
    r = diameter / 2
    a = math.pi * r**2
    return price/a



pizzaOne = int(input("Enter the price of first pizza:"))
pizzaTwo = int(input("Enter the price of second pizza:"))
diameterOne = int(input("Enter the diameter of the first pizza:"))
diameterTwo = int(input("Enter the diameter of the second pizza:"))

pizza1 = pizza(pizzaOne, diameterOne)
pizza2 = pizza(pizzaTwo, diameterTwo)
if pizza1 < pizza2:
    print("First pizza provides better value for money")
if pizza2 < pizza1:
    print("Second pizza provides better value for money")

print("the value of first pizza per m^2 is: ", pizza1, " dollars.")
print("the value of second pizza per m^2 is: ", pizza2, " dollars.")

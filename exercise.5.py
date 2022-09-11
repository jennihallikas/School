# 1 Dice
import random

rolls1 = int(input("How many times to roll the dice?"))
dice = []
sum = 0
rolls2 = 0
while rolls2 != rolls1:
    rolls2 = rolls2+1
    dice.append(int(random.randint(1,6)))
for x in dice:
    sum = sum+x
print("The sum of rolls is: " + str(sum) +" ("+ str(dice)+")")

# 2 List descending order
list = []
number = (input("Enter integer numbers: "))
if number != "":
    number = int(number)
    while number != "":
        list.append(number)
        number = (input("Enter integer numbers or leave an empty string to quit: "))
        if number != "":
            number=int(number)
        else:
            break
list.sort(reverse=True)
print("The 5 greatest numbers in descending order are: ")
for s in list[0:5]:
    print(s)

# 3 Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
num = int(input("Enter a number: "))
if num == 1:
    print(num, "is a prime number")
elif num < 0:
    print(num, "is not a prime number")
number = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            number = True
if number:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# 4
citylist = []
input("Enter names of 5 cities: ")
for x in range(0,5):
    citylist.append(input("Enter city name: "))
print("\n The 5 cities are:")
for x in citylist:
    print(x)

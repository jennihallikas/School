# 1: Fish length
length = int(input("What's the length of the zander in cm?"))
def checklength(length):
    if length >= 42:
        print ("Good for you!")
    elif length < 42:
        print (f"Release the fish back into the lake, the fish is {42 - length:.2f} centimeters too small")

checklength(length)

# 2: Cabin class
cabin_class = str(input("Enter the cabin class LUX, A, B or C?"))
LUX = "LUX"
A = "A"
B = "B"
C = "C"
if cabin_class == LUX:
    print ("The cabin is an upper-deck cabin with a balcony.")
elif cabin_class == A:
    print ("The cabin is above the car deck, equipped with a window.")
elif cabin_class == B:
    print ("The cabin is a windowless cabin above the car deck.")
elif cabin_class == C:
    print ("The cabin class is a windowless cabin below the car deck.")
else:
    print ("error: Invalid cabin class.")

# 3: Hemoglobin
gender = str(input("Enter your gender: "))
HB = int(input("Enter the HB level: "))


def CheckHB(HB):
    if (gender == 'Male' and HB > 167) or (gender == 'Female' and HB > 155):
        print("Hemoglobin value is high");
    elif (gender == 'Male' and HB < 134) or (gender == 'Female' and HB < 117):
        print("Hemoglobin value is low")
    else:
        print("Hemoglobin value is normal")


CheckHB(HB)

# 4: Leap year
Year = int(input("Enter the number: "))


def CheckLeap(Year):
    if ((Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0)):
        print("Given Year is a leap Year");
    else:
        print("Given Year is not a leap Year")


CheckLeap(Year)

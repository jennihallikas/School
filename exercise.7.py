"""
seasonList = ("Spring", "Summer", "Autumn", "Winter")
monthNumber = int(input("Input a number of a month"))
if monthNumber == 12 or 1 or 2:
    print(seasonList[3])
elif monthNumber == 3 or 4 or 5:
    print(seasonList[0])
elif monthNumber == 6 or 7 or 8:
    print(seasonList[1])
elif monthNumber == 9 or 10 or 11:
    print(seasonList[2])



setNames = set()
while 1:
    name = input("Enter name: ")
    if name in setNames:
        print("Existing name")
    elif name != setNames:
        setNames.add(name)
        print("New name")
    elif name == "":
        break
"""
airport = {}

airport["EFHK"] = "Helsinki-Vantaa"
airport["OJAM"] = "Amman Queen Alia"

def newAirport(airport):
    ICAO = str(input("Insert ICAO code: "))
    name = str(input("Insert airport name: "))

    airport[ICAO] = name
    print("Airport added.\n")

    return airport


def existingAirport(airport):
    ICAO = str(input("Insert airport ICAO code : "))

    if ICAO in airport:
        print(f"Airport name: {airport[ICAO]}")
    else:
        print("Airport not found.")

    return airport


while True:
    print("(1) Enter new airport")
    print("(2) Fetch existing airport's information")
    print("(3) Quit")

    userInput = input("Choose your option (1/2/3): ")
    print("")

    if userInput == "1":
        newAirport(airport)
    elif userInput == "2":
        existingAirport(airport)
    elif userInput == "3":
        break
    else:
        print("Invalid input. Please try again.\n")
        continue










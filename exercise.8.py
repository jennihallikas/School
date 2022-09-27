import mysql.connector
from tabulate import tabulate
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def getAirport(icao):
    #sql += " WHERE name= ident'" + last_name + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{icao}';")
    #cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, tablefmt="fancy_grid"))
    print(result)
    return


icao = input("Enter ICAO: ")
getAirport(icao)

# 2

print("Input Area code to get iformation: ")

from tabulate import tabulate

def getInfoById(id):
    sql = "SELECT type, name from airport where iso_country ='" + \
        id + "' order by type desc"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
    result = cursor.fetchall()
    print(tabulate(result, tablefmt="fancy_grid"))
    print(result)
    return

areaCode = input("Input the area code: ")
getInfoById(areaCode)

#3
from geopy import distance
def getInfoBy(icao):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    list = []
    for x in cursor:
        list.append(x)
    return result

icao = input("Enter 1st ICAO: ")
a = getInfoBy(icao)[0]
icao = input("Enter 2nd ICAO: ")
b = getInfoBy(icao)[0]
print(a, b)
print(f"The distance between is {distance.distance(a, b).km:.2f} km")


#
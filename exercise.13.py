from flask import Flask, request, Response
import json
import mysql.connector



app = Flask(__name__)
@app.route("/prime")
def prime(num):
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = False
    isPrime = True

    response = {
    "Number" : num,
    "isPrime" : isPrime,
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#2
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
)

app = Flask(__name__)

@app.route('/airport/<string:icao>')

def airport(icao):
    cursor = connection.cursor()
    cursor.execute = "SELECT name, municipality from airport where ident = '" + icao + "'"
    result = cursor.fetcall
    print(result)
    name = result[0]
    location = result[1]

    try:
        response = {
    "Airport" : name,
    "Location" : location,
    "ICAO" : icao
 }
        return response
    except:
        return "Request could not be completed."


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
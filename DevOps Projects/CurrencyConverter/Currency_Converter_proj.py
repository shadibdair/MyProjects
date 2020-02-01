import urllib .request, json

import data

with urllib.request.urlopen(
        "https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=996c3f238644dabafc06") as url:
    data = json.loads(url.read())

results = data['results']
ILS_USD = results['ILS_USD']
currency_value = ILS_USD['val']

print("\t\t\tWelcome to currency converter")
try:
    amount = float(input("Please enter an amount of Shekeles to convert: "))
    print("Result is: ", float(amount*currency_value))
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")
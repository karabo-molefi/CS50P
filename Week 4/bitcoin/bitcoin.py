import requests
import sys
import json

n = sys.argv

if len(n) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        float(n[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.RequestException:
            sys.exit("Something went wrong, please try agin.")
        else:
            o = response.json()

            rate =  o["bpi"]["USD"]["rate_float"]
            rate = float(rate)

            dollar = n[1]
            dollar = float(dollar)

            amount = rate * dollar


            print(f"${amount:,.4f}")
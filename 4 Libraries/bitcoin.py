import requests,json,sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = json.dumps(response.json()["bpi"]["USD"]["rate"]).replace("\"","").replace(",","")
        print(f"${float(rate)*float(sys.argv[1]):,}",end = "")
    except requests.RequestException:
        pass


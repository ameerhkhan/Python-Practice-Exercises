# Using Yahoo finance API

import json
from urllib.request import urlopen # can also use requests library


# Yahoo! Finance API for currency conversion has been shut down since 2017.
with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.read()

# print(source) # --> string containing json info.

data = json.loads(source)

print(json.dumps(data, indent=2))

usd_rates = dict()

print(len(data['list']['resources']))

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price # name of currency as key and conversion rate as value.
    print(name, price)

print(usd_rates['USD/EUR'])

#convert 50 usd to Euros
print(50 * float(usd_rates['USD/EUR']))
print(50 * float(usd_rates['USD/INR']))
print(50 * float(usd_rates['USD/PKR']))

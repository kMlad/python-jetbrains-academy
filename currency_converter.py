# write your code here!
import json
from requests import get

# fetching data
my_currency = input()
url = f'http://www.floatrates.com/daily/{my_currency}.json'
res = get(url)
json_data = json.loads(res.content)

# processing and caching data
cache = dict()
if my_currency != 'usd':
    cache['usd'] = json_data['usd']
if my_currency != 'eur':
    cache['eur'] = json_data['eur']

while True:
    converted_currency = input()
    if converted_currency == '':
        break
    currency_amount = int(input())

    print('Checking the cache...')
    if converted_currency in cache.keys():
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[converted_currency.lower()] = json_data[converted_currency.lower()]
    message = f'You received {cache[converted_currency.lower()]["rate"] * currency_amount} {converted_currency.upper()}.'
    print(message)

import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


def get_data():
  url = "https://www.iban.com/currency-codes"
  req = requests.get(url)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  rows = soup.select("tbody > tr")
  countries = []

  for row in rows:
    name = row.select("td")[0].text
    code =  row.select("td")[2].text
    if name and code:
      if name != "No universal currency":
        country_info = {
          'name' : name.capitalize(),
          'code' : code
        }
        countries.append(country_info)

  return countries



def select(countries):
  try:
    num = int(input("\n#: "))
  
    if(num<0 or num>len(countries)):
      print('Choose a number from the list.')
      return select(countries)
    
    else:
      print(f'{countries[num]["name"]}')
      return countries[num]["code"] 
      

  except:
    print("That wasn't a number.")
    return select(countries)


def ask_amount(first, second):
  try:
    print(f"\nHow many {first} do you want to convert to {second}?")
    amount = int(input())
    return amount
  
  except:
    print("That wasn't a number.")
    return ask_amount(first, second)

def converter(amount_from):  
  url =f"https://transferwise.com/gb/currency-converter/{first}-to-{second}-rate?amount={amount_from}"
  req = requests.get(url)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  rate = soup.select_one("#rate")['value']
  amount_to = amount_from * float(rate)

  currency_from = format_currency(amount_from, first, locale="ko_KR")
  currency_to = format_currency(amount_to, second, locale="ko_KR")

  print(f"{currency_from} is {currency_to}")



# Main

countries = get_data()

print('Welcome to CurrencyConvert PRO 2000')

for index, country in enumerate(countries):
  print(f'# {index} {country["name"]}')


print("\nWhere are you from? Choose a country by number.")
first = select(countries)

print("\nNow choose another country.")
second = select(countries)


amount_from = ask_amount(first, second)
converter(amount_from)
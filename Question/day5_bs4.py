import os
import requests
from bs4 import BeautifulSoup

def make_data():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"
  req = requests.get(url)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  countries = soup.select("tbody > tr")
  countries_info = []

  for i in range(len(countries)):
    country_currency = countries[i].select("td")[1].text

    if(country_currency != 'No universal currency'):
      country_info = {
        'name' : countries[i].select("td")[0].text.capitalize(),
        'currency_code' : countries[i].select("td")[2].text
      }
      countries_info.append(country_info)

  return countries_info


def print_main(countries_info):
  print('Hello! Please choose select a country by number:')

  for i in range(len(countries_info)):
    print(f'# {i} {countries_info[i]["name"]}')


def check_currency_code(total, countries_info):
  try:
    num = int(input("#: "))

    if(num<0 or num>total):
      print('Choose a number from the list.')
      return check_currency_code(total, countries_info)
    
    else:
      print(f'You chose {countries_info[int(num)]["name"]}\nThe currency code is {countries_info[int(num)]["currency_code"]}')  

  except:
    print("That wasn't a number.")
    return check_currency_code(total, countries_info)


infomation = make_data()
print_main(infomation)
check_currency_code(len(infomation), infomation)
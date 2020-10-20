import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


companies_request = requests.get(alba_url)
companies_soup = BeautifulSoup(companies_request.text, "html.parser")

goods = companies_soup.select("#MainSuperBrand > ul > li > a.goodsBox-info")

for good in goods:
  name = good.select_one("span.logo > img")['alt'],
  link = good['href']
  print(name)
  jobs_request = requests.get(link)
  jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")

  job_count = jobs_soup.select_one("#NormalInfo > p > strong").text
  

  if job_count != '0':  
    table = jobs_soup.select("#NormalInfo > table > tbody > tr")
    summary_table = jobs_soup.select("#NormalInfo > table > tbody > tr.summaryView")
    jobs = [x for x in table if x not in summary_table]

    f = open(f'{name[0]}.csv', 'w', encoding='utf-8')

    for job in jobs:
      location = job.select_one("td.local").text
      title = job.select_one("td.title > a > span.company").text
      part_time = job.select_one("td.data > span").text   
      pay = ''.join([x.text for x in job.find_all('span')])
      post_time = job.select_one("td.regDate").text
      wr = csv.writer(f)
      wr.writerow([location, title, part_time, pay, post_time])

    f.close()
  

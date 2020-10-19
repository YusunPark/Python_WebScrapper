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
  # company = {
  #   'name' : good.select_one("span.company").text,
  #   'link' : good['href']
  # }
  name = good.select_one("span.company").text,
  link = good['href']

  jobs_request = requests.get(link)
  jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")

  job_count = jobs_soup.select_one("#NormalInfo > p.jobCount > strong").text
  print(job_count)

  if job_count != 0:  
    table = jobs_soup.select("#NormalInfo > table > tbody > tr")
    summary_table = jobs_soup.select("#NormalInfo > table > tbody > tr.summaryView")
    jobs = [x for x in table if x not in summary_table]

    f = open(f'{name}.csv', 'w', encoding='utf-8')
    print(job_count)

    for job in jobs:
      location = job.select_one("td > div.L_MyAd_").text
      title = job.select_one("td > a > span.company").text
      part_time = job.select_one("td > span.time").text
      money_type = job.select_one("td > span.hour").text 
      pay = job.select_one("td > span.number").text
      post_time = job.select_one("td.regDate > strong").text

      print(title)

      wr = csv.writer(f)
      wr.writerow([location, title, part_time, money_type+pay, post_time])

    f.close()

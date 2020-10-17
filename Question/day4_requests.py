import os
import requests

def edit_url(urls=[]):
  edit_urls=[]
  for url in urls:
    edit_url = url.lower().replace(" ","")

    if("http://" not in edit_urls and ".com" not in edit_url):
      edit_urls.append(f"http://{edit_url}.com")

    elif("http://" not in edit_urls):
      edit_urls.append("http://"+edit_url)

    elif(".com" not in edit_url):
      edit_urls.append(edit_url+".com")

    else:
      pass
  return edit_urls
    
def closing_commet():
  print("Do you want to start over? y/n")
  answer = input().lower()

  if(answer == 'n'):
    print("k. bye!")

  elif(answer == 'y'):
    os.system(f"python {os.path.basename(__file__)}")

  else:
    print("That's not a valid answer")
    closing_commet()
  


print(f"Welcome to {os.path.basename(__file__)}!")
print("Please write a URL or URLs you want to cleck. (separated by comma)")


urls = input().split(',')

# url 전처리
edit_urls = edit_url(urls)

# single input
if(len(urls) == 1):  
  try:
    res = requests.get(edit_urls[0])
    print(f"{edit_urls[0]} is up!")

  except requests.exceptions.RequestException as e:
    print(f"{urls[0]} is not a valid URL.")

# multi input
else:
  for url in edit_urls:
    try:
      res = requests.get(url)
      print(f"{url} is up!")
    except requests.exceptions.RequestException as e:
      print(f"{url} is down!")

# ending
closing_commet()
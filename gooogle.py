import requests
import html5lib
from bs4 import BeautifulSoup
import csv
import time
import html
import random

fake_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Brave/1.35.103",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Brave/1.36.112",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Brave/1.37.121",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4958.80 Safari/537.36 Brave/1.38.130",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4982.113 Safari/537.36 Brave/1.39.145",
]


def get_random_user_agent():
    ua = fake_user_agents
    return random.choice(ua)

headers = {
    'User-Agent': get_random_user_agent()
  }





def get_name(container) :
  name=str(container.find('h3',attrs={'class':'tAxDx'}))
  start=name.find('>')
  name=name[start+1:]
  end=name.find('<')
  name=name[:end]
  if name =='' :
     return 'NA'
  else :
    return name

def get_price(container) :
  price=str(container.find('span',attrs={'class':'a8Pemb OFFNJ'}))
  start=price.find('>')
  price=price[start+1:]
  end=price.find('<')
  price=price[:end]
  if price=='' : 
     return 0
  else :
    return ''.join(price[1:].split(','))

def get_rating(container) : 
  rating=str(container.find('span',attrs={'class':'Rsc7Yb'}))
  start=rating.find('>')
  rating=rating[start+1:]
  end=rating.find('<')
  rating=rating[:end]
  if rating!='' or rating =='Non' :
      return rating
  else :
      return 0

def get_count_rating(container)  :
  no_of_rating=str(container.find('span',attrs={'class':'QIrs8'}))
  start=no_of_rating.find('>')
  no_of_rating=no_of_rating[start+1:]
  end=no_of_rating.find('<') 
  try :
      no_of_rating=no_of_rating[:end].split()[5]
      return ''.join(no_of_rating.split(','))
  except :
      return 0

def get_url(container) :
  prod_url=str(container.find('a',attrs={'class':'shntl'}))
  start = prod_url.find('href=')
  prod_url = prod_url[start + 6:]
  end = prod_url.find('"')
  prod_url = prod_url[:end]
  prod_url = "https://www.google.com"+prod_url
  prod_url = prod_url.replace('&amp;', '&')
  if prod_url=='' :
     return 'NA'
  else : 
    return prod_url

def get_image (container) :
  a=str(container.find('a',attrs={'class':'Lq5OHe eaGTj translate-content'}))
  start = a.find('href=')
  a = a[start + 6:]
  end = a.find('"')
  a = a[:end]
  img_url = 'https://www.google.com' + a
  img_html = requests.get(img_url , headers=headers)
  soup = BeautifulSoup(img_html.content, 'html.parser')
  image = soup.find('img' , attrs={'class':'sh-div__image sh-div__current'})
  image=str(image)
  start = image.find('src="')
  image = image[start + 5:]
  end = image.find('"')
  image = image[:end]
  if image =='' : 
      image = soup.find('div' , attrs={'class':'HE4Qgd'})
      image=str(image)
      start = image.find('src="')
      image = image[start + 5:]
      end = image.find('"')
      image = image[:end]
  if image=='' :
     return 'NA'
  else :
    return image

def extract_data(containers) :
  count =15
  det=[]
  c = 0
  for i in range (len(containers)) :
    temp=[]
    temp.append(get_name(containers[i]))
    temp.append(get_price(containers[i]))
    temp.append(get_rating(containers[i]))
    temp.append(get_count_rating(containers[i]))
    temp.append(get_image(containers[i]))
    time.sleep(2)
    temp.append(get_url(containers[i]))
    det.append(temp)
    c+=1
    if (c==count) :
       break

    
    
  fields = ['Name', 'Price', 'Average Rating', 'No of Ratings', 'ImageURL','Product URL']
  with open("google.csv", 'w' , encoding='utf-8', newline='') as google:
    csvwriter = csv.writer(google)
    csvwriter.writerow(fields)
    csvwriter.writerows(det)

def init(brand,product) :
  google_url = 'https://www.google.co.in/search?q=' + brand + " " + product + "&tbm=shop"
  html = requests.get(google_url, headers=headers)
  soup = BeautifulSoup(html.content, 'html.parser')
  amazonhtml = open ('google.html' , 'w' ,encoding='utf-8')
  amazonhtml.write(soup.prettify())
  amazonhtml.close()
  containers = soup.find_all('div', attrs={'class': 'i0X6df'})
  extract_data(containers)



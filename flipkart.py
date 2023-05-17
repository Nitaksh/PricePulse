import requests
import html5lib
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
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
def getlinks(link):
  links = []
  for i in link:
    a = str(i)
    start = a.find('href=')
    a = a[start + 6:]
    end = a.find('"')
    a = a[:end]
    links.append('https://www.flipkart.com' + a)
  if links=="":
    return "NA"
  else:
    return links



def getname(soup):
  name = str(soup.find('span', attrs={'class': 'B_NuCI'}))
  start = name.find('>')
  name = name[start + 1:]
  end = name.find('<')
  name = name[:end]
  if name=="":
    return "NA"
  else:
    return name




def getprice(soup):
  price = str(soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}))
  start = price.find('>')
  price = price[start + 2:]
  end = price.find('<')
  price = price[:end]
  if price=="":
    return 0
  else:
    return ''.join(price.split(','))
  


def getrating(soup):
  avg_rating = str(soup.find('span', attrs={'class': '_2_R_DZ'}))
  start = avg_rating.find('<span class="_2_R_DZ"><span><span>')
  avg_rating = avg_rating[start + 34:]
  end = avg_rating.find('Ratings')
  avg_rating = avg_rating[:end]
  if avg_rating=="":
    return 0
  else:
    return ''.join(avg_rating.split(','))
  

def getavgrating(soup):
  rating = str(soup.find('div', attrs={'class': '_3LWZlK'}))
  start = rating.find('>')
  rating = rating[start + 1:]
  end = rating.find('<')
  rating = rating[:end]
  if rating=="":
    return 0
  else:
    return rating
  
  

def getimage(soup):
  image = str(soup.find('img', attrs={'class': '_396cs4 _2amPTt _3qGmMb'}))
  start = image.find('src="')
  image = image[start + 5:]
  end = image.find('"')
  image = image[:end]
  if image=="":
    return "NA"
  else:
    return image


def get_product_info(links):
  product_info = []
  count = 0
  for link in links:
    product_html = requests.get(link, headers=headers)
    soup = BeautifulSoup(product_html.content, 'html5lib')
    name = getname(soup)
    if (name == None):
      continue
    price = getprice(soup)
    rating = getavgrating(soup)
    noofratings = getrating(soup)
    image = getimage(soup)
    product_info.append([name, price, rating, noofratings, image, link])
    count += 1
    if (count == 15):
      break
  return product_info


def flipkart_file(product_info):
  fields = [
    'Name', 'Price', 'Average Rating', 'No of Ratings', 'Image URL',
    'Product URL'
  ]
  with open("flipkart.csv", 'w' , encoding='utf-8',newline='') as flipkart:
    csvwriter = csv.writer(flipkart)
    csvwriter.writerow(fields)
    csvwriter.writerows(product_info)

def init(brand,product) :
  flipkart_url = 'https://www.flipkart.com/search?q=' + brand + " " + product
  html = requests.get(flipkart_url, headers=headers)
  soup = BeautifulSoup(html.content, 'html5lib')
  amazonhtml = open ('flipkart.html' , 'w' ,encoding='utf-8')
  amazonhtml.write(soup.prettify())
  amazonhtml.close()
  link = soup.find_all('a', attrs={'class': 's1Q9rs'})
  if link == []:
    link = soup.find_all('a', attrs={'class': '_1fQZEK'})
  if link == []:
    link = soup.find_all('a', attrs={'class': 'IRpwTa'})
  links = getlinks(link)
  product_info = get_product_info(links)
  flipkart_file(product_info)
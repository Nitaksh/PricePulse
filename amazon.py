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
    a.replace('&amp;','&')
    links.append('https://www.amazon.in/' + a)
  if links =="":
    return "NA"
  else:
    return links


def getname(soup):
  name = str(soup.find('span', attrs={'id': 'productTitle'}))
  start = name.find('>')
  name = name[start + 1:]
  end = name.find('<')
  name = name[:end]
  if name=="":
      return "NA"
  else:
      return name


def getprice(soup):
  price = str(soup.find('span', attrs={'class': 'a-price-whole'}))
  start = price.find('>')
  price = price[start + 1:]
  end = price.find('<')
  price = price[:end]
  if price=="":
      return 0
  else:
      return price


def getrating(soup):
  rating = str(soup.find('span', attrs={'id': 'acrCustomerReviewText'}))
  start = rating.find('>')
  rating = rating[start + 1:]
  end = rating.find('<')
  rating = rating[:end]
  if rating=="":
      return 0
  else:
      return rating.split(' ')[0]
    
  
  


def getavgrating(soup):
  avg_rating = str(
    soup.find('span',attrs={'class': 'reviewCountTextLinkedHistogram noUnderline'}))
  start = avg_rating.find('title="')
  avg_rating = avg_rating[start + 7:]
  end = avg_rating.find('"')
  avg_rating = avg_rating[:end]
  if avg_rating=="":
      return 0
  else:
      return avg_rating.split(' ')[0]

    
  
def getimage(soup):
  image = str(soup.find('img', attrs={'id': 'landingImage'}))
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
    price = getprice(soup)
    rating = getrating(soup)
    avg_rating = getavgrating(soup)
    image = getimage(soup)
    product_info.append([name, price, avg_rating, rating,image, link])
    count += 1
    if (count == 15):
      break
  return product_info


def amazon_file(product_info):
  fields = [
     'Name', 'Price', 'Average Rating', 'No of Ratings', 'Image URL',
    'Product URL'
  ]
  with open("amazon.csv", 'w' , encoding='utf-8' , newline='') as amazon:
    csvwriter = csv.writer(amazon)
    csvwriter.writerow(fields)
    csvwriter.writerows(product_info)

def init(brand, product) :  
  amazon_url = 'https://www.amazon.in/s?k=' +brand+ "+"+ product
  html = requests.get(amazon_url, headers=headers)
  soup = BeautifulSoup(html.content, 'html5lib')
  amazonhtml = open ('amazon.html' , 'w' ,encoding='utf-8')
  amazonhtml.write(soup.prettify())
  amazonhtml.close()
  link = soup.find_all(
    'a',
    attrs={
      'class':
      'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
    })
  links = getlinks(link)
  product_info = get_product_info(links)
  amazon_file(product_info)
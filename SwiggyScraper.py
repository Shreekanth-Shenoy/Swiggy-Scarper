from bs4 import BeautifulSoup
import requests
import csv
import itertools

allCities=[]

#####  To scrape allCities in swiggy database    ####
url=("https://www.swiggy.com/")
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
for city in soup.findAll("a", {"class": "_3TjLz b-Hy9"}):
  allCities=allCities+list((city.text).split("\n "))


testCities=['manipal','udupi']
resturants=[]
ratings=[]
avgPrices=[]
cuisines=[]
result=[]

#####  To scrape resturants in allCities    ####
#for city in allCities:

####    To scrape resturants in testCities    ####
for city in testCities:
  for page in range(1,20):
      url=("https://www.swiggy.com/"+city+"?page="+str(page))
      req=requests.get(url)
      soup=BeautifulSoup(req.text, "html.parser")
      for hotel_name in soup.findAll("div", {"class": "nA6kb"}):
        resturants=resturants+list((hotel_name.text).split("\n "))

      for rating in soup.findAll("div", {"class": "_9uwBC"}):
        ratings=ratings+list((rating.text).split("\n "))

      for avgPrice in soup.findAll("div", {"class": "nVWSi"}):
        avgPrices=avgPrices+list((avgPrice.text).split("\n "))

      for cuisine in soup.findAll("div", {"class": "_1gURR"}):
        cuisines=cuisines+list((cuisine.text).split("\n "))



  result=result+list(zip(itertools.repeat(city.capitalize()),resturants, ratings, avgPrices, cuisines)) 

####  Saving the data in CSV    ####
filename='restaurants.csv'
with open(filename, 'w', newline='', encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(['City','Restaurant', 'Ratings', 'Average Price', 'Cuisines'])
    for res in result:
        writer.writerow(res)
    f.close()
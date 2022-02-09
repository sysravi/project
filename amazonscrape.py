from bs4 import BeautifulSoup
import csv
import requests
from urllib.error import HTTPError


#defining headers for data fetch from website
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

#containers to store data
titles = []
imageurls = []
prices = []
details = []


# Function to extract Product Title
def get_title(soup):
     
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
 
        # Inner NavigableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip()
 
        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()
 
    except AttributeError:
        title_string = ""   
 
    return title_string

# Function to extract Product Image
def get_img(soup):
    try:
        tag=soup.find('div',{'id':'img-canvas'})
        imgtag = tag.img
        iurl = imgtag.attrs['src']
 
    except AttributeError:
        iurl = ""  
 
    return iurl

# Function to extract Product Price
def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'price'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price

# Function to extract Details
def get_detail(soup):
    try:
        detail = soup.find("div", attrs={'class':'a-section a-spacing-small a-padding-small'})
        detail_span = detail.span
        detail_txt = detail_span.contents
 
    except AttributeError:
        detail_txt = ""  
 
    return detail_txt


with open("amazonscraping.csv") as file:
    data_reader = csv.reader(file)
    for line in data_reader:
        if len(line[2])>=10:
            url = ("https://www.amazon."+line[3]+"/dp/"+line[2])
            webpage = requests.get(url,headers=HEADERS)
            soup = BeautifulSoup(webpage.content,'html.parser')
            #print(soup.prettify())
            titles.append(get_title(soup))
            imageurls.append(get_img(soup))
            prices.append(get_price(soup))
            details.append(get_detail(soup))

        else:
            print("https://www.amazon."+line[3]+"/dp/"+line[2])

#print(len(titles))
#print(len(prices))
#print(len(details))
#print(len(imageurls))
#for given dataset, len = 94
#dictionary to be written to JSON file
products=[]
for t,i,p,d in zip(titles,imageurls,prices,details):
    prod = {'prodTitle':t,'prodImgURL':i, 'prodPrice':p, 'prodDetails':d}
    products.append(prod)
print(products)

import json

with open("sample.json","w") as outfile:
    json.dump(products,outfile)
import csv
from http import server
import json
import jsonpickle
from json import JSONEncoder
from lib2to3.pgen2 import driver
from re import template
from tokenize import Special
from unittest import result
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def get_url(search_term):
    template = 'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/{}/c/{}-423144840?q=%3Arelevance%3AisOnPromotion%3AOn%2BPromotion&text=&pageSize=10'

    search_term = search_term.replace(' ', '_')

    url = template.format(search_term,search_term)

    url +='&page={}'
    
    return url

def extract_record(item):
    
    try:
        before_price =  item.find('div',{'class':'oldPrice'}).text.strip()
    except AttributeError:
        before_price = ""

    try:
        special_text = item.find('div',{'class':'promotionContainer promotionsShortText'}).text.strip()
    except AttributeError:
        special_text = ""    

    yield{
        "description" : item.find('div',{'class':'item-name'}).text.strip(),
        "url": item.a.img.get('src'),
        "now_price" : item.find('div',{'class':'currentPrice'}).text.strip(),
        "vaild_date" : "",
        "before_price" : before_price,
        "special_text" : special_text
    }

    result = yield

    return result

def main(search_term):

    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    records = []
    url = get_url(search_term)
    
    print(url)

    driver.get(url.format(0))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    pagecount = soup.find('div',{'class':'totalResults'}).text.replace('SHOWING 1-10 OF ','').strip()
    pagecount = round(int(pagecount)/10)

    for page in range(0,1):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'class': 'productCarouselItem js-product-carousel-item'})
    
        for item in results:
            records.append(extract_record(item))

    driver.close()

    dataJSON = jsonpickle.encode(records, unpicklable=False)
    JSONData = json.loads(dataJSON)

    with open('pickandpay'+search_term+'.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(jsonpickle.decode(dataJSON))

main('household-and-cleaning')
# main('frozen-food')
# main('milk-dairy-and-eggs')
# main('fresh-fruit-and-vegetables')
# main('fresh-fruit-and-vegetables')

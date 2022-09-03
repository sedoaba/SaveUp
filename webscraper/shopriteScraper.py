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
    template = 'https://www.shoprite.co.za/specials?q=%3AspecialsRelevance%3AallCategories%3A{}%3AbrowseAllStoresFacet%3AbrowseAllStoresFacet%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff'

    search_term = search_term.replace(' ', '_')

    url = template.format(search_term)

    url +='&page={}'

    return url

def extract_record(item):

    try:
        vaild_date = item.find('span',{'class':'item-product__valid'}).text
    except AttributeError:
         vaild_date = ""

    try:
        before_price =  item.find('span',{'class':'before'}).text.strip()
    except AttributeError:
        before_price = ""

    try:
        special_text = item.find('span',{'class':'item-product__message__text'}).text.strip()
    except AttributeError:
        special_text = ""

    yield {
            "description" : item.a.img.get('title'),
            "url": 'https://www.shoprite.co.za' + item.a.img.get('data-original-src'),
            "now_price" : item.find('span',{'class':'now'}).text.strip(),
            "vaild_date" : vaild_date.replace("\xa0"," ").replace("\u00a0"," ").strip(),
            "before_price" : before_price,
            "special_text" : special_text
    }

    result = yield

    return result

def main(search_term):
    #chrome_executable = Service(executable_path='C:\\geckodriver-v0.27.0-win64\\geckodriver.exe', log_path='NUL')
    #driver = webdriver.Firefox(service=chrome_executable)
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    #driver = webdriver.Firefox(executable_path='C:\\geckodriver-v0.27.0-win64\\geckodriver.exe')

    records = []
    url = get_url(search_term)

    driver.get(url.format(0))
    soup = BeautifulSoup(driver.page_source,'html.parser')
    pagecount = soup.find('p',{'class':'total-number-of-results pull-right'}).text.replace(' items','').strip().replace(',','')
    pagecount = round(int(pagecount) / 20)

    for page in range(0,1):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source,'html.parser')
        results = soup.find_all('figure',{'class':'item-product__content'})

        for item in results:
            records.append(extract_record(item))
        
    driver.close()

    dataJSON = jsonpickle.encode(records, unpicklable=False)
    JSONData = json.loads(dataJSON)

    with open('shopritedata_'+search_term+'.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(jsonpickle.decode(dataJSON))

    # with open('shopritedata_'+search_term+'.json', 'w') as json_file:
    #     json.dump(JSONData, json_file)

main('chicken')
# main('health_and_beauty')
# main('household')
# main('baby')
# main('electronics')
# main('fresh_meat_and_poultry')
# main('canned_food')
# main('spices')
# main('frozen_vegetables')
# main('fresh_fruit')
# main('fresh_vegetables')
# main('soups_and_stocks')
# main('male_spray_deodorant')
# main('female_spray_deodorant')
# main('body_lotion_moisturiser_and_scrub')
# main('frozen_food')
# main('medicine')
# main('porridge_maize_meal_and_pap')
# main('rice_pasta_noodles_and_cous_cous')
# main('squash_concentrates_and_cordials')
# main('milk_butter_and_eggs')
# main('gravies_sauces_and_pastes')
# main('spirits_and_liqueurs')
# main('soft_drinks')
# main('spirit_and_wine_coolers')
# main('beer_and_cider')

# dont use yet
# main('skincare')
# main('food_cupboard')
# main('food')
# main('drinks')
# main('cleaning')

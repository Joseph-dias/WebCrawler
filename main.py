from bs4 import BeautifulSoup
import time
import lxml
import requests
from Scraper import Scraper

dataScraper = Scraper('https://www.louderwithcrowder.com/')

print(dataScraper.scrape())

#data = requests.get('https://www.louderwithcrowder.com/').text  # Pulling html text

#soup = BeautifulSoup(data, 'lxml')

#widgets = soup.find_all('div', class_ = 'widget__head')

#for w in widgets:
 #   link = w.find('a')
  #  sub_data = requests.get(link['href']).text  # Get sub page data
 #   articleText = BeautifulSoup(sub_data, 'lxml')
 #   print(link['aria-label'])
 #   print(articleText.find('div', class_ = 'body-description').find('p').text)
 #   print('')
 #   print('')
from Scraper import Scraper

class Starter:

    def Start(self):
        url = input('Starter Site: ')
        dataScraper = Scraper(url)
        print(dataScraper.scrape())



Starter().Start()
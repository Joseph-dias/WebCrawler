from bs4 import BeautifulSoup
import requests

class Scraper:
    myUrl = ''
    def __init__(self, myurl):
        self.myUrl = myurl

    def scrape(self):
        data = requests.get(self.myUrl).text  # Pulling html text
        soup = BeautifulSoup(data, 'lxml')
        title = soup.find('title').text

        toReturn = {title}

        for div in soup.find('body').find_all(['main', 'div', 'section', 'p', 'a', 'span']):
            words = div.text.split(' ')
            for word in words:
                FinalWord = ''.join(l for l in word if l.isalnum())
                if len(FinalWord) > 4:
                    toReturn.add(FinalWord)

        return toReturn
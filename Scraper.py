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

        toReturn = title

        for div in soup.find_all('div'):
            proceed = True
            if 'id' in div and 'class' in div and div['id'].find('nav') == -1 and div['class'].find('nav') == -1:
                pass
            elif 'id' in div and div['id'].find('nav') == -1:
                pass
            elif 'class' in div and div['class'].find('nav') == -1:
                pass
            else:
                proceed = False

            if proceed:
                for tag in div.find_all(['p', 'a']):
                    words = tag.text.split(' ')
                    for word in words:
                        if len(word) > 4:
                            toReturn = toReturn + ' ' + word

        return toReturn
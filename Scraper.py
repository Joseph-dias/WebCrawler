from bs4 import BeautifulSoup
import requests

class Scraper:
    TagsToScrape = ['main', 'div', 'section', 'p', 'a', 'span']

    isMatch = False
    myUrl = ''
    foundUrls = set()  # Holding more urls to visit
    def __init__(self, myurl):
        self.myUrl = myurl

    def scrape(self, keyword):
        data = requests.get(self.myUrl).text  # Pulling html text
        soup = BeautifulSoup(data, 'lxml')
        title = soup.find('title').text

        pageWords = set()

        titleWords = title.split(' ')
        for word in titleWords:  # Splitting title words
            theWord = ''.join(l for l in word if l.isalnum())
            pageWords.add(theWord)

        for div in soup.find('body').find_all(self.TagsToScrape, recursive=False):
            words = div.text.split(' ')
            for word in words:
                FinalWord = ''.join(l for l in word if l.isalnum())
                if len(FinalWord) > 4:
                    pageWords.add(FinalWord)
            pageWords.update(self.recurse(div))

        self.isMatch = len([k for k in pageWords if keyword.lower() in k.lower()]) > 0

        for link in soup.find_all('a'):
            if 'http' in link['href']:
                self.foundUrls.add(link['href'])

    def recurse(self, div):
        toReturn = set()

        for myDiv in div.find_all(self.TagsToScrape, recursive=False):
            words = myDiv.text.split(' ')
            for word in words:
                FinalWord = ''.join(l for l in word if l.isalnum())
                if len(FinalWord) > 4:
                    toReturn.add(FinalWord)
            toReturn.update(self.recurse(myDiv))
        return toReturn

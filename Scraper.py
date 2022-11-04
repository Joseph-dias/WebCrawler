import bs4
from bs4 import BeautifulSoup
import requests
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class Scraper:
    TagsToScrape = ['main', 'div', 'section', 'p', 'a', 'span']

    isMatch = False
    myUrl = ''
    foundUrls = set()  # Holding more urls to visit
    def __init__(self, myurl):
        self.myUrl = myurl

    def scrape(self, keyword):
        data = requests.get(self.myUrl, timeout=5).text  # Pulling html text
        soup = BeautifulSoup(data, 'lxml')
        title = soup.find('title')

        splitWords = keyword.split(' ')
        finalSplitWords = []

        for w in splitWords:
            finalSplitWords.append(''.join(l for l in w if l.isalnum()))

        pageWords = set()

        if title is not None:
            title = title.text
            titleWords = title.split(' ')
            for word in titleWords:  # Splitting title words
                theWord = ''.join(l for l in word if l.isalnum())
                pageWords.add(theWord)

        if soup.find('body') is None:
            return

        for div in soup.find('body').find_all(self.TagsToScrape, recursive=False):
            if div.name == 'header' or div.name == 'footer':  # Skip header and footer tags
                continue
            try:
                if div['href'].startswith('http'):
                    continue
            except KeyError:
                pass
            words = div.text.split(' ')
            for word in words:
                FinalWord = ''.join(l for l in word if l.isalnum())
                if len(FinalWord) > 4:
                    pageWords.add(FinalWord)
            pageWords.update(self.recurse(div))

        for sw in finalSplitWords:
            self.isMatch = len([k for k in pageWords if sw.lower() in k.lower()]) > 0
            if self.isMatch:
                break

        for link in soup.find_all('a', attrs={'href' : True}):
            if link['href'].startswith('http'):
                self.foundUrls.add(link['href'])

    def recurse(self, div):
        toReturn = set()

        for myDiv in div.find_all(self.TagsToScrape, recursive=False):
            if myDiv.name == 'header' or myDiv.name == 'footer':
                continue
            try:
                if myDiv['href'].startswith('http'):
                    continue
            except KeyError:
                pass
            words = myDiv.text.split(' ')
            for word in words:
                FinalWord = ''.join(l for l in word if l.isalnum())
                if len(FinalWord) > 4:
                    toReturn.add(FinalWord)
            toReturn.update(self.recurse(myDiv))
        return toReturn

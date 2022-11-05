import requests

from Scraper import Scraper
from TimeKeeper import TimeKeeper
from collections import deque
import re
import time

class Starter:

    matching = set()
    queuedLinks = set()
    crawlPath = deque()  # Queue of links to crawl over

    def Start(self):
        pattern = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

        # Scraping first site
        url = input('Starter Site: ')
        while not pattern.match(url):
            print("INVALID SITE")
            url = input('Try Again: ')

        keyword = input('Search: ')
        validSearch = len([s for s in keyword.split(' ') if len(''.join(l for l in s if l.isalnum())) < 4]) == 0
        while not validSearch:
            print('Invalid search.  Each word must be at least four characters.')
            keyword = input('Try Again: ')
            validSearch = len([s for s in keyword.split(' ') if len(''.join(l for l in s if l.isalnum())) < 4]) == 0


        length = None
        minutesGiven = False
        while not minutesGiven:
            mins = input('How many minutes to run: ')
            try:
                length = TimeKeeper(int(mins))
                minutesGiven = True
            except ValueError:
                pass


        self.queuedLinks.add(url)

        print('')
        print('Matches:')

        keepCrawling = True
        while keepCrawling:
            try:
                dataScraper = Scraper(url)
                dataScraper.scrape(keyword)
                if dataScraper.isMatch and url not in self.matching:  # Add link to output if keyword found
                    self.matching.add(url)
                    print(url)
                self.crawlPath.extend([u for u in dataScraper.foundUrls if u not in self.queuedLinks])
                self.queuedLinks.update(dataScraper.foundUrls)
            except requests.ConnectionError: # Catch exceptions about the requests and move on
                pass
            except requests.Timeout:
                pass
            except requests.RequestException:
                pass
            if len(self.crawlPath) == 0 or length.hasPassed():
                keepCrawling = False
            else:
                url = self.crawlPath.popleft()
        if len(self.matching) == 0:
            print('NOTHING FOUND')
        else:
            print('')
            print('END OF RESULTS')


try:
    program = Starter()
    program.Start()
except KeyboardInterrupt:
    print('')
    print('')
    print('You exited...')
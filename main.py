from Scraper import Scraper
from collections import deque

class Starter:

    matching = set()
    queuedLinks = set()
    crawlPath = deque()  # Queue of links to crawl over

    def Start(self):
        # Scraping first site
        url = input('Starter Site: ')
        keyword = input('Search: ')

        print('')
        print('Matches:')

        keepCrawling = True
        while keepCrawling:
            dataScraper = Scraper(url)
            dataScraper.scrape(keyword)
            if dataScraper.isMatch:  # Add link to output if keyword found
                self.matching.add(url)
                print(url)
            self.crawlPath.extend([u for u in dataScraper.foundUrls if u not in self.queuedLinks])
            self.queuedLinks.update(dataScraper.foundUrls)
            if len(self.crawlPath) == 0:
                keepCrawling = False
            else:
                url = self.crawlPath.popleft()
        if len(self.matching) == 0:
            print('NOTHING FOUND')



program = Starter()

program.Start()
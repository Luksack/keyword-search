import requests
from bs4 import BeautifulSoup
from lxml import html
import re

class KeywordSearch:
    def __init__(self, site_url):
        self.keyword = input("Please insert the keyword You are looking for: " + '\n' + '> ')
        self.keyword_count = 0
        self.site_url = site_url

    def scrap_html(self, url):
        scrap = requests.get(url)
        if scrap.status_code == 200:
            self.search_keyword(scrap.text)
        else:
            print("Error: Site is unavaible.")

    def search_keyword(self, html):
        soup = BeautifulSoup(html, 'lxml')
        paragraph = soup.findAll(text=re.compile(self.keyword))
        print(paragraph)
        for element in paragraph:
            if self.keyword in element:
                self.keyword_count += 1



    def start(self):
        print("Searchnig...Please Wait")
        self.scrap_html(self.site_url)


scraper = KeywordSearch("https://news.ycombinator.com/item?id=16492994")
scraper.start()
print("You were looking for %s" % scraper.keyword)
print("There are: " + str(scraper.keyword_count))

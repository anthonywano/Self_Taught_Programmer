import urllib.request
from bs4 import BeautifulSoup
import ssl

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            print(tag)
            url = tag.get("href")
            if url is None:
                continue
                #print("None")
            elif "html" in url:
                print("\n" + url)


ssl._create_default_https_context = ssl._create_unverified_context
news = "https://news.google.com/"
Scraper(news).scrape()

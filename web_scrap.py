from bs4 import BeautifulSoup as bs
import requests
import re

class WebScrapingImages:
    def __init__(self, url):
        self.url = url

    def get_images(self):
        soup = bs(requests.get(self.url).content, 'html.parser')
        tag = soup.find_all('img', class_='img-responsive')
        for tag in tag:
            print(tag.get('src'))

class WebScrapingText:
    def __init__(self, url):
        self.url = url

    def get_text(self):
        soup = bs(requests.get(self.url).content, 'html.parser')
        tag = soup.find_all('p')
        for tag in tag:
            print(tag.text)


class WebScrapingLink:
    def __init__(self, url):
        self.url = url

    def get_links(self):
        soup = bs(requests.get(self.url).content, 'html.parser')
        # print(soup)
        tag = soup.find_all('a', href=re.compile(r'^https://')) 
        # print(tag)     
        for tag in tag:
            print(tag.get('href'))
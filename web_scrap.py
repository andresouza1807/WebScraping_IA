from bs4 import BeautifulSoup as bs
import requests
import re

class WebScrapingImages:
    def __init__(self, url):
        self.url = url

    def get_images(self,output_file):
        soup = bs(requests.get(self.url).content, 'html.parser')
        tags = soup.find_all('img', src=re.compile(r'^http://'))
        with open(output_file,'w', encoding='utf-8') as file:
            for tag in tags:
                file.write(tag.get('src') + '\n')

class WebScrapingText:
    def __init__(self, url):
        self.url = url

    def get_text(self,output_file):
        soup = bs(requests.get(self.url).content, 'html.parser')
        tags = soup.find_all('p')
        with open(output_file, 'w', encoding='utf-8') as file:
            for tag in tags:
                file.write(tag.text)        


class WebScrapingLink:
    def __init__(self, url):
        self.url = url

    def get_links(self,output_file):
        soup = bs(requests.get(self.url).content, 'html.parser')
        # print(soup)
        tag = soup.find_all('a', href=re.compile(r'^https://')) 
        # print(tag) 
        with open(output_file, 'w', encoding='utf-8') as file:    
            for tag in tag:
                file.write(tag.get('href') + '\n')
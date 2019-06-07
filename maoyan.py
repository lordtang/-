# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:23:18 2019

@author: T
"""

import requests
from lxml import etree

class Maoyan(object):
    def  __init__(self):
        self.base_url = "https://maoyan.com/films"
        self.headers = {
                "Accept-Encoding":"gzip",
                "User-Agent":"Mozilla5.0/"
        }
        self.proxies = {"http":"182.35.84.67:9999"}
        self.films=[]
    
    def get_page(self):
        res = requests.get(url=self.base_url,headers = self.headers,proxies = self.proxies)
        res.encoding="utf-8"
        return res.text
    
    def parse_page(self):
        html = self.get_page()
        parse_HTML = etree.HTML(html)
        film_node = parse_HTML.xpath('//dd')
        print(len(film_node))
        for film in film_node:
            film_name=film.xpath('./div[@class="channel-detail movie-item-title"]/@title')
            grade_int = film.xpath('./div[@class="channel-detail channel-detail-orange"]/i[@class="integer"]')
            grade_fra = film.xpath('./div[@class="channel-detail channel-detail-orange"]/i[@class="fraction"]')
            if grade_fra:
                grade = grade_int[0].text+grade_fra[0].text
            else:
                grade="None"
            print(grade)
            d = { 
                    "filmname":film_name[0],
                    "grade":grade,
                }
            self.films.append(d)      
        
    def run(self):
        self.parse_page()
        print(self.films)
        
maoyan = Maoyan()
maoyan.run()



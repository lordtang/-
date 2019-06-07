# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:25:21 2019

@author: T
"""

#链家房产
import requests
import re
import time

class LianjiaSpyder(object):
    def __init__(self):
        self.page = 1
        self.url = "https://cd.lianjia.com/ershoufang/pg{}/"
        self.proxies = {"https":"115.53.16.61:9999"}
        self.headers = {
        "Accept-Encoding":"gzip",
        "User-Agent":"Mozilla5.0/"
        }
        

    def get_page(self,url):
        res = requests.get(url,proxies = self.proxies,headers = self.headers)
        res.encoding = "utf-8"
        return res.text
    
    def get_info(self,html):
        p = re.compile('class="houseInfo">.*?data-el="region">(.*?) </a>.*?<div class="priceInfo">.*?<span>(.*?)</span>')
        r_list = p.findall(html)
        return r_list
        
        
    def run(self):
        while True:
            url = self.url.format(self.page)
            time.sleep(1)
            html = self.get_page(url)
            r_list = self.get_info(html)
            print(r_list)
            self.page+=1
            if self.page==100:
                break
        
test = LianjiaSpyder()
test.run()
        
        
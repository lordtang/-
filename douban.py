# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:20:40 2019

@author: T
"""

import requests
import selenium
import json
import csv

url = "https://movie.douban.com/j/chart/top_list?"
params = {
        "type":"11",
        "interval_id":"100:90",
        "action":"",
        "start":"0",
        "limit":"100"
        }

headers = {
        "Accept-Encoding":"gzip",
        "User-Agent":"Mozilla5.0/"
        }
proxies = {"http":"182.35.84.67:9999"}

res = requests.get(url=url,params=params,headers=headers,proxies=proxies)
res.encoding="utf-8"
html = res.text
#print(html)
html = json.loads(html)
films_info = []
for films in html:
    film_name = films["title"]
    score = films['score']
    d = {
            "name":film_name,
            "score":score,
            }
    films_info.append(d)
    
for films in films_info:
    with open('doubantop100.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([films['name'],films['score']])

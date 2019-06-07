# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:33:04 2019

@author: T
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import requests

url = "https://www.douyu.com/directory/all"
driver = webdriver.PhantomJS()
driver.get(url)
driver.find_element_by_class_name("layout-Module-lable is-active").click()

time.sleep(5)
driver.save_screenshot("网游.png")
headers = {
        "Accept-Encoding":"gzip",
        "User-Agent":"Mozilla5.0/"
        }
proxies = {"http":"182.35.84.67:9999"}
html = requests.get(url=url,headers=headers,proxies=proxies)
html.encoding='utf-8'
html=html.text
#html = driver.execute_script("return document.documentElement.outerHTML")

# 不要用 driver.page_source，那样得到的页面源码不标准

#html = driver.page_source
print(html)
while True:
#    创建解析对象
    soup = bs(html,'lxml')
    names = soup.find_all('h2',{"class":"DyListCover-user"})
    hots = soup.find_all('span',{"class":"DyListCover-hot"})
    print(len(names))
    for name,num in zip(names,hots):
#        name和num都是对象，有一个get_text方法
        name = name.get_text()
        num = num.get_text()
        print('-----------------------')
        time.sleep(2)
        print("name:"+name,"hot:"+num)

#    调用方法获取查找元素、

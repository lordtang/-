# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:10:14 2019

@author: T
"""

import requests
from lxml import etree

class BaiduTieba(object):
    def __init__(self):
        self.headers = {
        "Accept-Encoding":"gzip",
        "User-Agent":"Mozilla5.0/"
        }
        self.proxies = {"https":"120.79.5.147:80"}
        self.url = "http://tieba.baidu.com/f?kw=%D0%A3%BB%A8"
        self.params = {"wd":"校花"}
        
    def get_html(self,url):
        res = requests.get(verify=False,url=url,headers = self.headers,proxies = self.proxies)
        res.encoding = "utf-8"
        html = res.text
#        print(html)
        return html
    
    def get_tie_url(self):
        self.tie_url = []
        html = self.get_html(self.url)
        self.parseHTML = etree.HTML(html)
        urls = self.parseHTML.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/@href')
        for url in urls:
            self.tie_url.append("http://tieba.baidu.com"+url)
        return self.tie_url
        
        
    def get_pic_url(self):
        pic_url = []
        for url in self.get_tie_url():
            tie_html = self.get_html(url)
            parseHTML = etree.HTML(tie_html)
            urls = parseHTML.xpath('//img[@class="BDE_Image"]/@src')
            if urls:
                pic_url+=urls
        return pic_url
    
    def save_pic(self):
        urls = self.get_pic_url()
        for url in urls:
            res = requests.get(url=url,headers=self.headers,proxies=self.proxies,verify=False)
            res.encoding="utf-8"
            pic_bin = res.content
            pic_name = url[-10:]
            print("正在保存{}".format(pic_name))
            with open('./pic/'+pic_name,'wb') as f:
                f.write(pic_bin)
                
    def change_page(self,start,end):
        for page in range(start,end):
            print('***************获取第{}页***************'.format(page))
            page = page*50
            self.url=self.url[0:40]+"&pn="+str(page)
            self.save_pic()
            
        
        
        
    def run(self):
        self.change_page(11,13)
        



bd = BaiduTieba()
bd.run()
        
    
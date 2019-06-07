# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:25:50 2019

@author: T
"""

import requests
import re
import csv
import random

def get_ip():
    url = "https://www.xicidaili.com"
    headers = {
        "Accept-Encoding":"gzip",
        "User-Agent":"Mozilla5.0/"
        }
    proxies = {"http":"121.233.206.44:9999"}
    xici = []
    res = requests.get(url,headers = headers,proxies=proxies)
    res.encoding="utf-8"
    p = re.compile('<tr class="odd">.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td class="country">.*?<td>(.*?)</td>',re.S)
    r_list = p.findall(res.text)
    for ip in r_list:
        if ip[2] in ["HTTP","HTTPS"]:
            key = ip[2]
            value = ip[0]+':'+ip[1]
            write_csv(key,value)
            ip = {key:value}
            xici.append(ip)
            
    ip = random.choice(xici)
    return ip
        
def write_csv(key,value):
    #打开csv文件，注意编码格式
    with open('ip.csv','a',newline='',encoding="gb18030") as f:
        writer = csv.writer(f)
#        创建writer,写入数据
        writer.writerow([key,value])
        
        
if __name__ == "__main__":
    ip = get_ip()
    print(ip)



# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:50:23 2019

@author: T
"""

import baseSpyder
import random
import re
import user_agent


def CrawMovieInfo(url):
    '''
    抓取猫眼数据
    '''
    headers=[("User-Agent",random.choice(user_agent.UA))]  
    print("Headers:"+headers[0][1])
    html = baseSpyder.downloadHtml(url,headers = headers)
    reg = '<div class="movie-item-info">[\s\S]*?title="([\s\S]*?)" data-act[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">上映时间：([\s\S]*?)</p>[\s\S]*?<div class="movie-item-number score-num">'
    pattern = re.compile(reg)
    res = re.findall(pattern,html)
    for info in res:
        name = info[0].split()[0]
        star = info[1].split()[0]
        releasetime = info[2].split()[0]
        with open("maoyan.txt",'a') as f:
            f.write('name:'+name+'\r\n'+'star:'+star+'\r\n'+'releasetime:'+releasetime+'\r\n'+'\r\n-----------------------------------------------\r\n')
        print(name,star,releasetime,end='\r\n')
    
if __name__ == "__main__":
    url = 'https://maoyan.com/board/4?offset='
    for i in range(10):
        print('正在爬取'+url+str(i*10))
        CrawMovieInfo(url+str(i*10))



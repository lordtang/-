# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:50:23 2019

@author: T
"""

import baseSpyder
import random
import re
from lxml import etree
import user_agent
import multiprocessing
import json
import urllib
import myPyMysql
import time


urls = []



def CrawMovieInfo():
    '''
    抓取猫眼数据
    '''
    des = input("请输入目的地>>")
    
    if not des:
        print("目的地不能为空")
        return

    parms = {
        "t":"guides",
        "q":des
    }
    parms = urllib.parse.quote(des)
    url = 'http://www.mafengwo.cn/search/q.php?'+'&q='+parms+'&t=guides'
    print(url)
    headers=[("User-Agent",random.choice(user_agent.UA))]  
    html = baseSpyder.downloadHtml(url,headers = headers)
    print(type(html))
    # for item in get_one_page(html):
    get_url(html)
    for url in urls:
        html = baseSpyder.downloadHtml(url[0],headers = headers)
        time.sleep(2)
        print(type(html))
        get_info_from_html(html)

        # lock.acquire()
#        write2file(item)
        # write2Sql(item)
        # lock.release()
    

def write2file(item):
    with open('.\maoyan2.txt','a',encoding='gb18030') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
        
def write2Sql(item):
    sqlHelper = myPyMysql.DBHelper()
    sql = "INSERT INTO `maoyan`.`maoyan_top` ( `name`, `star`, `release`) VALUES (%s,%s,%s);"
    print(item['name'])
    params = (item['name'],item['star'],item['releasetime'])
    print(params)
    sqlHelper.execute(sql,params)

def get_url(html):
    tree = etree.HTML(html)
    res = tree.xpath('//div[@class="att-list"]/ul/li')
    for info in res:
        c_url = info.xpath('./div/div/h3/a/@href')
        urls.append(c_url)
        
def get_info_from_html(html):
    tree = etree.HTML(html)
    title = tree.xpath('//div[@class="l-topic"]/h1/text()')
    print(title)

def get_one_page(html):
    tree = etree.HTML(html)
    res = tree.xpath('//div[@class="att-list"]/ul/li')
    for info in res:
        title = info.xpath('./div/div/h3/a/span/text()')
        content = info.xpath('./div/div/h3/a/@href')
        print(title)
        print(content)
        # film = {'name:':info[0].strip(),
        #       'star:':info[1].strip(),
        #       'releasetime:':info[2].strip(),
        #       }
        # print(film)
        # yield film
        
    

if __name__ == "__main__":
    CrawMovieInfo()
    print(urls)
#     manager = multiprocessing.Manager()
#     lock = manager.Lock()
    
# #    partial_CrawMovieInfo = functools.partial(CrawMovieInfo,lock)
#     pool = multiprocessing.Pool(2)
# #    pool.map(partial_CrawMovieInfo,[i for i in range(10)])
#     for i in range(10):
#         pool.apply_async(CrawMovieInfo, args=(lock,i))
#     pool.close()
#     pool.join()
#     print('over')





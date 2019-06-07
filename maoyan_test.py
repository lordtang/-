# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:50:23 2019

@author: T
"""

import baseSpyder
import random
import re
import user_agent
import multiprocessing
import json
import myPyMysql


def CrawMovieInfo(lock,offset):
    '''
    抓取猫眼数据
    '''
    url = 'https://maoyan.com/board/4?offset='+str(offset*10)
    print(url)
    headers=[("User-Agent",random.choice(user_agent.UA))]  
    html = baseSpyder.downloadHtml(url,headers = headers)
    
    for item in get_one_page(html):
        lock.acquire()
#        write2file(item)
        write2Sql(item)
        lock.release()
    

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

        

def get_one_page(html):
    reg = '<div class="movie-item-info">[\s\S]*?title="([\s\S]*?)" data-act[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">上映时间：([\s\S]*?)</p>[\s\S]*?<div class="movie-item-number score-num">'
    pattern = re.compile(reg)
    res = re.findall(pattern,html)
#    print(res)
    for info in res:
        film = {'name:':info[0].strip(),
              'star:':info[1].strip(),
              'releasetime:':info[2].strip(),
              }
        print(film)
        yield film
        
    

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    
#    partial_CrawMovieInfo = functools.partial(CrawMovieInfo,lock)
    pool = multiprocessing.Pool(2)
#    pool.map(partial_CrawMovieInfo,[i for i in range(10)])
    for i in range(10):
        pool.apply_async(CrawMovieInfo, args=(lock,i))
    pool.close()
    pool.join()
    print('over')





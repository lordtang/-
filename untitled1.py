# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:08:06 2019

@author: T
"""
from urllib import request,error
import time
import random

def downloadHtml(url,headers=[],proxy={},
                 timeout=None,decodeInfo="utf-8",num_retries=10,ues_proxy_ratio=5):
    '''
    一个完善的下载网页的逻辑
    支持User-Agent
    支持Proxies
    支持Headers
    超时的考虑
    编码问题，如果不是utf-8怎么处理
    服务器返回5xx的错误
    客户端出现4xx的错误
    考虑延时的问题
    '''
    time.sleep(random.ranint(1,3))
    
#    调整是否使用代理
    if random.randint(1,10) > ues_proxy_ratio:
        proxy=None
    
    html = None
#    创建ProxyHandler
    proxy_support=request.ProxyHandler(proxy)
#    创建openr
    opener = request.build_opener(proxy_support)
#    设置user-agent
    opener.add_handlers=headers
#    安装openr
    request.install_opener(opener)
    
    try:
#        可能出现编码异常，网络下载异常：客户端、服务器（404，403）
        res = request.urlopen(url)
        html = res.read().decode(decodeInfo)
        
    except UnicodeDecodeError:
        print("编码出错")
    except error.URLError or error.HTTPError as e:
        if hasattr(e,'code') and 400 <=e.code <500:
            print('客户端错误')
        elif hasattr(e,'code') and 500 <=e.code <600:
            print('正在尝试重新获取')
            if num_retries>0:
                time.sleep(int(200/num_retries))
                downloadHtml(url,headers,proxy,
                             timeout,decodeInfo,num_retries-1)
                
    return html
    
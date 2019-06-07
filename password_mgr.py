# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:35:41 2019

@author: T
"""

import urllib.request

server = '117.67.228.136:16819'
user = "309435365"
password="szayclhp"
url = "http://www.baidu.com"
#密码管理器对象
pwd = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd.add_password(None,server,user,password)

#创建处理器对象
proxy_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(proxy_handler)

req = urllib.request.Request(url)
res = opener.open(req)
html = res.read().decode("utf-8")
print(html)
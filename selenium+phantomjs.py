# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:36:47 2019

@author: T
"""

from selenium import webdriver
import requests


#创建打开phantomjs的对象
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

#获取网页截图
driver.save_screenshot("baidu.png")
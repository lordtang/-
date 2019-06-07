# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:54:55 2019

@author: T
"""

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com/')
res1 = driver.page_source.find('kw') #不能找到
res2 = driver.page_source.find('aaaaa') #能找到
res = driver.find_element_by_class_name("mnav").text
print(res1,res2,res)

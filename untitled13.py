# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:07:30 2019

@author: T
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.douyu.com/directory/all"

driver = webdriver.PhantomJS()
driver.get(url)
driver.save_screenshot("斗鱼直播.png")

time.sleep(3)
driver.find_element_by_class_name('dy-Pagination-next').click()
time.sleep(3)
driver.save_screenshot("下一页.png")




# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:05:43 2019

@author: T
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

import time

driver = webdriver.PhantomJS()
driver.get('https://accounts.douban.com/passport/login')
time.sleep(3)

user_name = '17602823158'
pwd = 'db147896'

wait = ui.WebDriverWait(driver,10)

wait.until(lambda driver:driver.find_element_by_name('username').send_keys(user_name))

driver.find_element_by_id('password').send_keys(pwd)
driver.find_element_by_class_name('btn btn-account').click()
time.sleep(2)
driver.save_screenshot("豆瓣test.png")

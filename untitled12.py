# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:58:23 2019

@author: T
"""

# 使用selenium和phantomJS浏览器登陆豆瓣的小演示

# 导入库
from selenium import webdriver

# 实例化一个浏览器对象
web = webdriver.PhantomJS()

# 请求页面
web.get("https://www.douban.com/")
# 保存截图
web.save_screenshot("douban.png")

# 搜索标签，输入账号
web.find_element_by_name("form_email").send_keys("豆瓣账号")
# 搜索标签，输入密码
web.find_element_by_name("form_password").send_keys("密码")
# 搜素标签，输入验证码
text = input("输入验证码")
web.find_element_by_name("captcha-solution").send_keys(text)
# 保存截图
web.save_screenshot("douban1.png")

# 点击登陆
web.find_element_by_class_name("bn-submit").click()
# 保存登陆后截图
web.save_screenshot("douban2.png")
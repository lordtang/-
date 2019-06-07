from selenium import webdriver
import time

#操作键盘鼠标
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

#查找搜索框位置，向输入框发送内容
driver.find_element_by_id("kw").send_keys(u'美女')
#driver.save_screenshot("美女.png")

#执行点击
driver.find_element_by_id('su').click()
time.sleep(2)
driver.save_screenshot("搜索.png")


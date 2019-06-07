
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs


url = "https://www.douyu.com/directory/all"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)


for i in range(5):
#    获取当前页面
    html = driver.page_source
#    创建解析对象
    soup = bs(html,'lxml')
#    bs匹配信息
    names = soup.find_all('h2',{"class":"DyListCover-user"})
    hots = soup.find_all('span',{"class":"DyListCover-hot"})
    for name,num in zip(names,hots):
#        name和num都是对象，有一个get_text方法
        name = name.get_text()
        num = num.get_text()
        print("name:"+name,"hot:"+num)
        
#    获取下一页    
    if driver.page_source.find("dy-Pagination-item-custom"):
        driver.find_element_by_class_name('dy-Pagination-next').click()
    else:
        break
    


        
        




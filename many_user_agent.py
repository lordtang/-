import urllib.request
import random

def load_baidu():
    url = "http://www.baidu.com"
    user_agent = ["Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
                  "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0",
                  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE",
                  "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"


    ]
    # 每次请求的浏览器都不一样
    random_user_agent = random.choice(user_agent)
    # 创建request对象
    request = urllib.request.Request(url)
    # 添加头部信息
    request.add_header("User-Agent",random_user_agent)
    # 发送请求，接收响应
    response = urllib.request.urlopen(request)
    print(response)#<http.client.HTTPResponse object at 0x05029D90>
    # 获取响应内容
    print(response.read())
    # 获取响应的头部信息，如果没有添加头部信息。则是Python-urllib/3.7
    print(request.get_header("User-agent"))


if __name__ == '__main__':
    load_baidu()
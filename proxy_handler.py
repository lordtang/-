import urllib.request

def create_proxy_handler():
    url = "https://www.csdn.net/"
    # 添加代理
    proxy = {
        "http":"http://110.167.204.78:8060",
        "http":"114.55.236.62:3128"
    }
    #$-------------------------------------------------------
    #付费ip的写法：
    proxy_pay = {
        "http":"username:pwd"
    }
    user_name = ''
    passwd = ''
    pass_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pass_manager.add_password(None,proxy_pay,user_name,passwd)
    #创建可以验证代理IP的处理器
    handler_auth = urllib.request.ProxyBasicAuthHandler(pass_manager)
    #创建openner
    opene_auth = urllib.request.build_opener(handler_auth)
    data = opene_auth.open('http://www.baidu.com')
    print(data.read())
    #$-------------------------------------------------
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 用处理器创建openner
    openner = urllib.request.build_opener(proxy_handler)
    # 用代理IP发送请求
    data = openner.open(url.read())
    print(data)

    #爬取自己公司的数据，做数据分析
    

    with open('csdn.html','wb') as f:
        f.write(data)

if __name__ == '__main__':
    create_proxy_handler()
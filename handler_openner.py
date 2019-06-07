import urllib.request

def handler_openner():
    # urllib.request.urlopen()
    url = "https://www.csdn.net/"
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的openner
    openner = urllib.request.build_opener(handler)
    # 用自己创建的openner来调用open方法
    response = openner.open(url)
    data = response.read()
    with open('csnd.html','wb') as f:
        f.write(data)

if __name__ == '__main__':
    handler_openner()
import urllib.request


def load_baidu():
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    # 创建请求对象
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
    # 动态添加headers信息
    request = urllib.request.Request(url)
    # 动态添加请求头
    request.add_header("User_Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36")
    data = response.read().decode("utf-8")
    with open("data.html","w",encoding="utf-8") as f:
        f.write(data)
    # 查看响应头信息
    # print(response.headers)
    #第二种打印headers的方法
    ret = request.get_header("User-Agent")
    # 获取完整的url
    final_url = request.get_full_url()

    print(final_url)
    #获取请求头信息
    request_headers = request.headers
    # print(request_headers)


if __name__ == '__main__':
    load_baidu()

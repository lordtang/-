import urllib.request


def proxy_user():
    url = "https://www.baidu.com/"
    proxy_list = [
        {"http": "140.143.156.166:1080"},
        {"http": "119.101.116.62:9999"},
        {"http": "125.40.79.66:8118"},
        {"http": "120.194.61.62:8060"},
        {"http": "218.76.253.201:61"},
        {"http": "193.112.15.70:8118"}
    ]
    for proxy in proxy_list:
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        openner = urllib.request.build_opener(proxy_handler)
        try:
            openner.open(url, timeout=1)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    proxy_user()

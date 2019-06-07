import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?wd="

    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"
    }
    # 将字典参数转换成计算机可以识别的码
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    # 拼接url
    final_url = url + str_params
    print(final_url)
    # end_url = urllib.parse.quote(final_url,safe=string.printable)
    # print(end_url)
    responde = urllib.request.urlopen(final_url)
    data = responde.read().decode("utf-8")
    print(data)


if __name__ == '__main__':
    get_params()

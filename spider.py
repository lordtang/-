import requests

class TiebaSpider(object):
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}".format(tieba_name,50)
    def parse_url(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
        response = requests.get(url,headers = headers)
        return response.content.decode(encoding='utf-8')

    def save(self):
        with open('tieba.html','w',encoding='utf-8') as f:
            f.write(self.parse_url(self.start_url))

    def  run(self):
        self.save()

if __name__ == '__main__':
    spider = TiebaSpider('lol')
    spider.run()



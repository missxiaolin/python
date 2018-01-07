from urllib import request

# https 会报错  导入ssl模块，把证书验证关了
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Spider():

    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        print(html)

    def go(self):
        self.__fetch_content()


spider = Spider()

spider.go()
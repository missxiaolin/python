# 正则模块
import re
# 发送
from urllib import request
# https 会报错  导入ssl模块，把证书验证关了
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Spider():
    # 请求url
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'

    # 发送请求
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    def __analysis(self, html):
        root_html = re.findall(Spider.root_pattern, html)
        print(root_html[0])

    def go(self):
        html = self.__fetch_content()
        self.__analysis(html)


spider = Spider()

spider.go()

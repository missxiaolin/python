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
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 发送请求
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    # 匹配主播名字和人气
    def __analysis(self, html):
        root_html = re.findall(Spider.root_pattern, html)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def go(self):
        html = self.__fetch_content()
        anchors = self.__analysis(html)


spider = Spider()

spider.go()

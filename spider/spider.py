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

    # 格式化
    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展示
    def __show(self, anchors):
        for anchor in anchors:
            print(anchor['name'] + '---' + anchor['number'])

    def go(self):
        html = self.__fetch_content()
        anchors = self.__analysis(html)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()

spider.go()

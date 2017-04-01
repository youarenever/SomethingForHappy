# -*- encoding:utf-8 -*-
import re
from bs4 import BeautifulSoup
from lxml import etree
import urllib2, urllib


class HttpConstructor(object):
    def __init__(self):
        pass

    @staticmethod
    def get_response(url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        try:
            response = urllib2.urlopen(request).read()  # 打开页面
            return response
        except urllib2.HTTPError:
            # print e.code
            return 0
            # print response

    @staticmethod
    def post_response():
        pass


class DataRule(object):
    def __init__(self):
        pass

    #判断末页
    @staticmethod
    def get_endpage(html):
        try:
            endre = re.compile("下一页|下页")
            endpage = re.findall(endre, html)
            # print endpage
            if unicode(endpage[0], "utf-8")==u"下一页":
                return 1
            # ht = BeautifulSoup(html, "lxml")
            # return ht.find_all(re.compile("下一页"))
        except Exception ,e:
            print e
            return 0

    def get_name(self,html):
        # ht = BeautifulSoup(html,"lxml")
        # return ht.div
        # print html
        # doc = html.fromstring(html2)
        # doc.text_content()
        # result = xml.xpath('//div[@class="Mid2L_con"]')
        # print doc.text_content()
        html_temp = etree.HTML(html)
        result = html_temp.xpath('//div[@class="Mid2L_con"]//img/@src')
        result2 = html_temp.xpath('//div[@class="Mid2L_con"]/p')
        # result = etree.tostring(result)
        print result2[0].text
        print result
        pass

    def get_image(self):

        pass


if __name__ == '__main__':
    html = HttpConstructor.get_response("http://www.gamersky.com/ent/201703/886782_2.shtml")
    t = DataRule()
    print t.get_name(html)
    # # print html
    # aa = DataRule.get_endpage(html)
    # print aa

    # print
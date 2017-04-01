# -*- encoding:utf-8 -*-
import re
from bs4 import BeautifulSoup
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

    def get_endpage(self, html):
        try:
            endre = re.compile("下一页")
            endpage = re.findall(endre, html)
            if unicode(endpage[0], "utf-8")==u"下一页":
                return 1
            # ht = BeautifulSoup(html, "lxml")
            # return ht.find_all(re.compile("下一页"))
        except Exception ,e:
            print e
            return 0

if __name__ == '__main__':
    html = HttpConstructor.get_response("http://www.gamersky.com/wenku/201703/883627_14.shtml")
    # print html
    t = DataRule()
    aa = t.get_endpage(html)
    print aa

    # print
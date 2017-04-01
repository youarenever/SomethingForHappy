# -*- encoding:utf-8 -*-
from time import sleep

from Items import HttpConstructor


# import logging

class HomepageUrl(object):
    def __init__(self):
        self.__url_list = []
        pass

    def start_url(self, url):
        pass

    def next_url(self, url, ex_str="_", palce=-6):
        HttpConstructor.get_response(url)
        for i in range(2, 200):
            print i
            sleep(0.05)
            url_temp = url[:palce] + ex_str + str(i) + url[palce:]
            if HttpConstructor.get_response(url_temp) == 0:  # 报错停止，一般是到最后一页了。
                print "break", i
                break
        pass


if __name__ == '__main__':
    hu = HomepageUrl()
    hu.next_url("http://www.gamersky.com/ent/201703/886782.shtml")
    pass

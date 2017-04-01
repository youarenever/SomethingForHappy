# -*- encoding:utf-8 -*-
# from time import sleep
from Items import HttpConstructor, DataRule


# import logging

class HomepageUrl(object):
    def __init__(self):
        self.__url_list = []
        pass

    def start_url(self, url):
        pass

    #拼接页数，不请求，不判断末页
    def next_url(self, url, ex_str="_", palce=-6):
        HttpConstructor.get_response(url)
        for i in range(2, 100):
            # sleep(0.05)
            url_temp = url[:palce] + ex_str + str(i) + url[palce:]
            print url_temp
            # response_all = HttpConstructor.get_response(url_temp)
            # if response_all == 0 or DataRule.get_endpage(response_all) == 0:  # 报错停止，或者最后一页，终止循环。
            #     print "break", i
            #     break
            self.__url_list.append(url_temp)
        return self.__url_list

if __name__ == '__main__':
    hu = HomepageUrl()
    print hu.next_url("http://www.gamersky.com/ent/201703/886782.shtml")
    pass

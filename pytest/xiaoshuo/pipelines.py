# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os
import time

class XiaoshuoPipeline(object):
    # def process_item(self, item, spider):
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    #
    #     return item
    # def __init__(self):
    #     self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # -*- coding: utf-8 -*-

        dir_path = "D:\\img\\" + time.strftime("%Y%m%d")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        path = dir_path+"\\"+item['name']+".jpg"
        print path
        urllib.urlretrieve(item['adr'], path)

        return item
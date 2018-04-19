# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MztPipeline(object):
    def process_item(self, item, spider):
        return item


# headers = {'User-Agent':Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240,
# 'Connection': 'Keep-Alive',
# 'Referer':http://www.mzitu.com/99566
# }
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from mzt.items import MztItem

class MztspiderSpider(CrawlSpider):
    name = 'mztspider'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all']
    img_urls=[]
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',),deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        # print response.url
        # pass
        item = MztItem()
        max_num = response.xpath()
        item['name'] = response.xpath()
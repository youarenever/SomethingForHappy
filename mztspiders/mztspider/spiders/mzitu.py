# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from mztspider.items import MztspiderItem


class MzituSpider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        img_urls = []
        item = MztspiderItem()
        item['name'] = response.xpath("")
        max_num = response.xpath("")

        for page in range(1, int(max_num)):
            page_url = response.url + '/' + str(max_num)
            yield Request(page_url, callback=self.get_img_url)

        item['img_urls'] = img_urls

    def get_img_url(self,response):
        img_url = response.xpath("")
        self.img_urls.append(img_url)



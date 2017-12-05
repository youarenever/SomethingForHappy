# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from xiaoshuo.items import XiaoshuoItem


class ExampleSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['zongheng.com']

    # 两种start url 设置方法：
    start_urls = ['http://www.gamersky.com/ent/']
    url_set = set()
    # def start_requests(self):
    #     yield Request('http://book.zongheng.com/rank.html',self.parse)

    def parse(self, response):
        temp_fsturl=""
        fsturl = response.xpath('//div[@class="Mimg"]/a[@class="img1"]/@href').extract()
        if len(fsturl):
            ExampleSpider.url_set.add(fsturl[0])
            temp_fsturl = fsturl[0][:-6]
            yield self.make_requests_from_url(fsturl[0])
            # print temp_fsturl
        #####保存当页的图片url和title#####
        if response.url.startswith(temp_fsturl):
            allPics = response.xpath('//div[@class="Mid2L_con"]/p')
            for p in allPics:
                item = XiaoshuoItem()
                picadr = p.xpath('./a/img/@src').extract()
                name = p.xpath('./text()').extract()
                if not len(name):
                    name.append(u"无题")
                if len(picadr):
                    item['adr'] = picadr[0]
                    item['name'] = name[0]
                    # print picadr[0]
                    # print name[0]
                    yield item


        ####提取下一页url
        urls = response.xpath('//div[@class="page_css"]/a/@href').extract()
        for url in urls:
            if url.startswith(temp_fsturl):
                if url not in ExampleSpider.url_set:
                    ####默认回调parse,并加入url_set以便后续去重
                    yield self.make_requests_from_url(url)
                    ExampleSpider.url_set.add(url)
                    print url


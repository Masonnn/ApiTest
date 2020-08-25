# -*- coding: utf-8 -*-
import scrapy


class SodasSpider(scrapy.Spider):
    name = 'sodas'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def parse(self, response):
        pass

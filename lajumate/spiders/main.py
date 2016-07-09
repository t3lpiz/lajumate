# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from lajumate.items import LajumateItem


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['lajumate.ro']
    start_urls = ['https://lajumate.ro/']

    rules = (
        Rule(LinkExtractor(allow=r'\w+\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = LajumateItem()
        localitate = response.xpath('//span[@id="location_city"]/a[0]/text()').extract()
        judet = response.xpath('//span[@id="location_city"]/a[1]/text()').extract()
        name = response.xpath('//h1[@itemprop="name"]/text()').extract()
        pret = response.xpath('//span[@id="price"]/text()').extract()
        valuta = response.xpath('//b[@itemprop="priceCurrency"]/text()').extract()
        descriere = response.xpath('//p[@itemprop="description"]/text()').extract()
        with open('rezultat.txt', 'a') as f:
            f.write(name[0] + '\n')
            f.write(judet[0] + '\n')
            f.write(pret[0] + valuta[0] + '\n')
            f.write(descriere[0] + '\n')
            f.write('\n')
            f.close()
        print(name[0], pret[0], valuta[0], judet[0], descriere[0])

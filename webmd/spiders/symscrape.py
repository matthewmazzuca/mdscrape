# -*- coding: utf-8 -*-
import scrapy

from webmd.items import WebmdItem


class SymscrapeSpider(scrapy.Spider):
    name = "symscrape"
    allowed_domains = ["http://www.webmd.com/a-to-z-guides/health-topics/default.htm"]
    start_urls = (
        'http://www.webmd.com/a-to-z-guides/health-topics/default.htm',
    )


    def parse(self, response):

    	sites = response.selector.xpath('//div[@class="a-to-z list"]/ul/li')
        items= []

    	for site in sites:
    		item = WebmdItem()
    		item['name']= site.xpath('a/text()').extract()
    		item['url']=site.xpath('a/@href').extract()
    		items.append(item)

    	print items

    	 

        pass

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

    	sel = selector.Selector(response)
		sites = sel.xpath('//div[@class="a-to-z list"]/ul/li').extract()
    	items = []

    	for site in sites:
    		item = WebmdItem()
    		item['name']= site.xpath('a/text()').extract()
    		item['url']=site.xpath('a/@href').extract()
    		items.append(item)

    	print items

    	 

        pass

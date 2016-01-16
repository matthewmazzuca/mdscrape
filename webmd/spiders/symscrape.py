# -*- coding: utf-8 -*-
import scrapy


class SymscrapeSpider(scrapy.Spider):
    name = "symscrape"
    allowed_domains = ["http://www.webmd.com/a-to-z-guides/health-topics/default.htm"]
    start_urls = (
        'http://www.webmd.com/a-to-z-guides/health-topics/default.htm',
    )


    def parse(self, response):



    	sites = response.xpath('//div[@class="a-to-z list"]/ul/li').extract()
    	items = []

    	for site in sites:
    		print site + '\n'

    	 

        pass

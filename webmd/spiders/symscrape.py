# -*- coding: utf-8 -*-
import scrapy

from webmd.items import WebmdItem


class SymscrapeSpider(scrapy.Spider):
    name = "symscrape"
    allowed_domains = ["www.webmd.com"]
    start_urls = (
        'http://www.webmd.com/a-to-z-guides/health-topics/default.htm',
    )

    def parse(self,response):
        site = response.selector.xpath('//div[@class="a-to-z alpha"]/ul/li')
        urls = []
        for href in site:
            url = href.xpath('a/@href').extract()
            url = "http://www.webmd.com" + url[0]
            urls.append(url)
        # print urls[0]

        for link in urls:
            # print link
            yield scrapy.Request(link, callback=self.parse_page)
        # yield scrapy.Request(url, self.parse_page)




    def parse_page(self, response):

    	sites = response.selector.xpath('//div[@class="a-to-z list"]/ul/li')
        items= []
        # print "the link is: " + self
        # print '\n'

    	for site in sites:
    		item = WebmdItem()
    		item['name']= site.xpath('a/text()').extract()
    		item['url']=site.xpath('a/@href').extract()
    		items.append(item)

    	return items

    	 

        

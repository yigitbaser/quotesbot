# -*- coding: utf-8 -*-
import scrapy


class SrealitySpider(scrapy.Spider):
    name = "sreality-spider"
    start_urls = [
        'https://www.sreality.cz/en/search/for-sale/apartments',
    ]

    def parse(self, response):
        # Extract listing names using CSS selector
        listing_names = response.css('div.property-title::text').extract()
        
        # Print the scraped listing names
        for name in listing_names:
            yield {
                'listing_name': name.strip()
            }
            
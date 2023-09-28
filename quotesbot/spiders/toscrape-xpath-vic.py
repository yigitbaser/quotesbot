# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpider(scrapy.Spider):
    name = 'toscrape-xpath-vic'
    start_urls = [
        'https://en.wikipedia.org/wiki/Victory_Day_(Turkey)',
    ]
    
    #"div.mw-content-container"
    #"span.mw-page-title-main::text"

    #"div.quote" --- '//div[@class="quote"]'
    #"small.author::text" --- './/small[@class="author"]/text()'

    def parse(self, response):
        for quote in response.xpath('//div[@class="mw-content-container"]'):
           # yield {
           #     'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
           #     'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
            #    'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
           # }
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")           
            print(quote.xpath('.//span[@class="mw-page-title-main"]/text()').extract_first())
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
      #  next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
      #  if next_page_url is not None:
      #      yield scrapy.Request(response.urljoin(next_page_url))



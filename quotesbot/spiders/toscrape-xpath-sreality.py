# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath-sreality'
    start_urls = [
        'https://www.sreality.cz/en/search/for-sale/apartments',
    ]

    def parse(self, response):
        for quote in response.xpath('//html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div'):
            yield {
               # 'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
              'author': quote.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[1]/div/div/span/h2/a/span').extract_first(),
              #  'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

      #  next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
    #    if next_page_url is not None:
      #      yield scrapy.Request(response.urljoin(next_page_url))


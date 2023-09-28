# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality"
    start_urls = [
        'https://www.sreality.cz/en/search/for-sale/apartments',
    ]

    def parse(self, response):
        print("Entered parser")
        print("AAAAAA")
        for quote in response.css("div.property.ng-scope"):
            print("Entered for loop")
            # yield {
            #     'text': quote.css("span.text::text").extract_first(),
            #     'author': quote.css("small.author::text").extract_first(),
            #     'tags': quote.css("div.tags > a.tag::text").extract()
            # }
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            #print(quote.css("span.name.ng-binding::text").extract_first())
            print("AAAAAAAAAAA")
            #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
         #   yield scrapy.Request(response.urljoin(next_page_url))



# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-victoryday"
    start_urls = [
        'https://en.wikipedia.org/wiki/Victory_Day_(Turkey)',
    ]

    def parse(self, response):
        for quote in response.css("div.mw-content-container"):
            # yield {
            #     'text': quote.css("span.text::text").extract_first(),
            #     'author': quote.css("small.author::text").extract_first(),
            #     'tags': quote.css("div.tags > a.tag::text").extract()
            # }
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
            yield {'text':quote.css("span.mw-page-title-main::text").extract_first()}
            print(quote.css("span.mw-page-title-main::text").extract_first())
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
       # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
          #  yield scrapy.Request(response.urljoin(next_page_url))

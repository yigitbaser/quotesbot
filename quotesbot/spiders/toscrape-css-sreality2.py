import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import db_functions

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality2"

    def __init__(self, *args, **kwargs):
        super(ToScrapeCSSSpider, self).__init__(*args, **kwargs)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options)


    def start_requests(self):
        urls = [#'https://www.sreality.cz/en/search/for-sale/apartments',
                #'https://www.sreality.cz/en/search/for-sale/apartments?page=2#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=3#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=4#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=5#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=6#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=7#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=8#z=4']

        for url in urls:
            print("\nEntered start request\n")
            self.driver.get(url)
            self.driver.implicitly_wait(5)
            body = self.driver.page_source
            #print(f"\n\n\n\n\nbody is: {str(body)}\n\n\n\n\n")
            url = self.driver.current_url
            #print(f"\n\n\n\n\nurl is: {str(url)}\n\n\n\n\n")
            #response = HtmlResponse(url=url, body=body, encoding='utf-8')
            yield scrapy.Request(url, callback=self.parse, meta={'body': body})
            #scrapy.Request(url, callback=self.parse, meta={'response': response})
        

    def parse(self, response):
        print("\nEntered PARSER\n")
        body = response.meta['body']  # Use the response object created in start_requests method
        response = HtmlResponse(url=response.url, body=body, encoding='utf-8')
        print(response.status)
        if response.css('div.property.ng-scope'):
            print("Response has 'div.property.ng-scope'")

        else:
            print("Response DOESNT HAVE 'div.property.ng-scope'")

        for index,item in enumerate(response.css('div.property.ng-scope')):
            #yield {'name': item.css('span.name.ng-binding::text').get()}
            #yield {'name': item.css('a.title').get()}
            print(f"\nAD #{index}")
            print(item.css('span.name.ng-binding::text').get()) 
            print(item.css('img::attr(src)').get())  
     
    def closed(self, reason):
        self.driver.quit()
      #  print("\n\n\n\n\nCLOSED\n\n\n\n\n")
        print("\nCLOSED\n")

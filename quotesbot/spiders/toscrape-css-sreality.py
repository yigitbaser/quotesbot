# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse

import logging
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)



class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality"

    def start_requests(self):
    # Initialize Selenium WebDriver

        self.driver = webdriver.Chrome()

        # Navigate to the website
        urls = ['https://www.sreality.cz/en/search/for-sale/apartments']
        for url in urls:
            self.driver.get(url)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
           
        #print("\n\n\n\n\nENTERED THE START REQUEST\n\n\n\n\n")
        # Wait for JavaScript to load content (adjust the wait time as needed)
        self.driver.implicitly_wait(10)

        # Get the page source after JavaScript has loaded
        page_source = self.driver.page_source

        # Create a Scrapy response object from the page source
        response = HtmlResponse(url=self.driver.current_url, body=page_source, encoding='utf-8')

        # Pass the response to your parsing method
        yield scrapy.Request(url=self.driver.current_url, callback=self.parse, meta={'response': response})

        # Close the browser
        self.driver.quit()

    def parse(self, response):
        #print("Entered PARSER")
        #print("\n\n\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n\n\n\n")

        body = self.driver.page_source
        url = self.driver.current_url
        new_response = HtmlResponse(url=url, body=body, encoding='utf-8', request=response.request)
        
        for item in new_response.css('div.property.ng-scope'):
            yield {
                'name': item.css('span.name.ng-binding::text').get()
            }





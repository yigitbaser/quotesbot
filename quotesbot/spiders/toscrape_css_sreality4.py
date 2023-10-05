import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import db_functions


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality4"

    def __init__(self, *args, **kwargs):
        super(ToScrapeCSSSpider, self).__init__(*args, **kwargs)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options)


    def start_requests(self):
        base_url = 'https://www.sreality.cz/en/search/for-sale/apartments?page={page}#z=4'
        urls = [base_url.format(page=i) for i in range(1, 9)]  # Generate URLs for pages 1 to 8


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
        body = response.meta.get('body', '')  # Use the response object created in start_requests method
        retry_count = response.meta.get('retry_count', 0)  # Get the current retry count
        
        body = response.meta['body']  # Use the response object created in start_requests method
        response = HtmlResponse(url=response.url, body=body, encoding='utf-8')
        print(response.status)

        if response.css('div.property.ng-scope'):
            print("Response has 'div.property.ng-scope'")
            for index, item in enumerate(response.css('div.property.ng-scope')):
                # yield {'name': item.css('span.name.ng-binding::text').get()}
                # yield {'name': item.css('a.title').get()}
                print(f"\nAD #{index}")
                print(item.css('span.name.ng-binding::text').get())
                print(item.css('img::attr(src)').get())

                item = { "name": item.css('span.name.ng-binding::text').get(),
                         "link": item.css('img::attr(src)').get()}
                db_functions.insert_item(item=item)

        else:
            print("Response DOESN'T HAVE 'div.property.ng-scope'")
            if retry_count < 5:  # Retry up to 5 times
                print(f"Retrying... Attempt {retry_count + 1}")
                yield scrapy.Request(
                    response.url, 
                    callback=self.parse, 
                    meta={'body': body, 'retry_count': retry_count + 1}, 
                    dont_filter=True
                    )
            else:
                print(f"Max retries reached for {response.url}. Not retrying further.")





       
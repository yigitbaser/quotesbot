import scrapy
from scrapy_splash import SplashRequest

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality-splash"
    
    def start_requests(self):
        urls = [
            'https://www.sreality.cz/en/search/for-sale/apartments',
            'https://www.sreality.cz/en/search/for-sale/apartments?page=2#z=4',
            'https://www.sreality.cz/en/search/for-sale/apartments?page=3#z=4',
            #... other URLs
        ]
        
        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 5})

    def parse(self, response):
        # print("\nEntered PARSER\n")
        # print(response.status)

        # for index, item in enumerate(response.css('div.property.ng-scope')):
        #     print(f"\nAD #{index}")
        #     print(item.css('span.name.ng-binding::text').get()) 
        #     print(item.css('img::attr(src)').get())
        def parse(self, response):
            print("\nEntered PARSER\n")
            print(response.status)
            print(response.text)  # print the entire response to debug

            for index, item in enumerate(response.css('div.property.ng-scope')):
                print(f"\nAD #{index}")
                
                # try to print some part of item to check if it’s being selected correctly
                print(item.get())
                
                print(item.css('span.name.ng-binding::text').get()) 
                print(item.css('img::attr(src)').get())  
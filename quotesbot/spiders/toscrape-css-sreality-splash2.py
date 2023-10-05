import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css-sreality-splash2"

    def __init__(self, *args, **kwargs):
        super(ToScrapeCSSSpider, self).__init__(*args, **kwargs)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options)

    def start_requests(self):
        urls = ['https://www.sreality.cz/en/search/for-sale/apartments','https://www.sreality.cz/en/search/for-sale/apartments?page=2#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=3#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=4#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=5#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=6#z=4',
                'https://www.sreality.cz/en/search/for-sale/apartments?page=7#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=8#z=4']

        for url in urls:
            self.driver.get(url)
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.property.ng-scope"))
                )
                body = self.driver.page_source
                yield scrapy.Request(url, callback=self.parse, meta={'body': body})
            except TimeoutException:
                self.logger.error(f"Timed out waiting for page to load: {url}")

    def parse(self, response):
        for index, item in enumerate(response.css('div.property.ng-scope')):
            yield {
                'name': item.css('span.name.ng-binding::text').get(),
                'image_url': item.css('img::attr(src)').get()
            }

    def closed(self, reason):
        self.driver.quit()

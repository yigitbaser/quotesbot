from scrapy.crawler import CrawlerProcess
from spiders.toscrape_css_sreality4 import ToScrapeCSSSpider


import settings

urls = ['https://www.sreality.cz/en/search/for-sale/apartments',
        'https://www.sreality.cz/en/search/for-sale/apartments?page=2#z=4',
        'https://www.sreality.cz/en/search/for-sale/apartments?page=3#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=4#z=4',
        'https://www.sreality.cz/en/search/for-sale/apartments?page=5#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=6#z=4',
        'https://www.sreality.cz/en/search/for-sale/apartments?page=7#z=4','https://www.sreality.cz/en/search/for-sale/apartments?page=8#z=4']

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
})


for url in urls:

    process.crawl(ToScrapeCSSSpider, start_url=url)

process.start()  # This will start the crawl using your spider
process.stop()  # Stop the process after one URL is scraped

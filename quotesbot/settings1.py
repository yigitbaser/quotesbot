from quotesbot.settings1 import *
BOT_NAME = 'quotesbot'

SPIDER_MODULES = ['quotesbot.spiders']
NEWSPIDER_MODULE = 'quotesbot.spiders'

LOG_LEVEL = 'INFO'


DOWNLOAD_DELAY = 4


DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'asdfqwer',
    'database': 'dbname'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quotesbot (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#Splash stuff
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

ITEM_PIPELINES = {
    'pipelines.PostgreSQLPipeline': 1,  # module_name should be the name of the module containing the PostgreSQLPipeline
}

process = CrawlerProcess(settings='settings')

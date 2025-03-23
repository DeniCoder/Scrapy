import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        pass

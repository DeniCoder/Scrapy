import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            relative_url = light.css('a').attrib['href']
            full_url = response.urljoin(relative_url)
            yield {
                'name' : light.css('div.lsooF span::text').get(),
                'price' : light.css('div.pY3d2 span::text').get(),
                'url' : full_url,
            }
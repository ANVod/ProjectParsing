import scrapy


class DivannewparsSpider(scrapy.Spider): #
    name = "divannewpars"
    allowed_domains = ["fetch"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')

        for divan in divans: #перебираем divans
            yield {
                'name': divan.css('div.lsooF span::text').get(),#вытаскиваем текст
                'price': divan.css('div.pY3d2 span::text').get(),#вытаскиваем текст
                'url': divan.css('a').attrib['href'] #вытаскиваем атрибут href
            }

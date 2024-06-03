import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        light_items = response.css('div._Ud0k')  # Подбираем правильный CSS селектор для элементов освещения

        for item in light_items:
            yield {
                'name': item.css('div.lsooF span::text').get(),  # Извлекаем название
                'price': item.css('div.pY3d2 span::text').get(),  # Извлекаем цену
                'url': response.urljoin(item.css('a').attrib['href'])  # Извлекаем URL и делаем его абсолютным
            }

        # Пагинация
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), self.parse)
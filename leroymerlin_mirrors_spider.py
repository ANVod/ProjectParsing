# Leroy Merlin. Scrapy. Web Scraping
import scrapy

class LeroymerlinMirrorsSpider(scrapy.Spider):
    name = "leroymerlin_mirrors" # название
    allowed_domains = ["leroymerlin.ru"] # домен
    start_urls = ["https://leroymerlin.ru/catalogue/zerkala-v-vannuyu-komnatu/"] # начальная страница

    def parse(self, response): # функция для парсинга
        # Обновленные селекторы для зеркал
        mirrors = response.css('div.f19v7pn1_plp.largeCard') # селектор для зеркал

        for mirror in mirrors: # для каждого зеркала
            yield {
                'name': mirror.css('span[data-qa="product-name"]::text').get(), # селектор для названия
                'price': mirror.css('span[data-qa="product-price"]::text').get(), # селектор для цены
                'url': response.urljoin(mirror.css('a[data-qa="product-link"]').attrib['href']) # селектор для ссылки
            }

        # Переход на следующую страницу, если она есть
        next_page = response.css('a[data-qa-pagination-item="right"]::attr(href)').get() #
        if next_page: # если есть
            yield response.follow(next_page, self.parse) # переход

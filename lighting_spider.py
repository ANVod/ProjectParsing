#PS05. Введение в Scrapy. Web Scraping
import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"  # Имя спарсера
    allowed_domains = ["divan.ru"] # Доменное имя
    start_urls = ["https://www.divan.ru/category/svet"] # Ссылка на первую страницу

    def parse(self, response): # Метод для парсинга
        light_items = response.css('div._Ud0k')  # Подбираем правильный CSS селектор для элементов освещения

        for item in light_items: # Перебираем элементы освещения
            yield {
                'name': item.css('div.lsooF span::text').get(),  # Извлекаем название
                'price': item.css('div.pY3d2 span::text').get(),  # Извлекаем цену
                'url': response.urljoin(item.css('a').attrib['href'])  # Извлекаем URL и делаем его абсолютным
            }

        # Пагинация
        next_page = response.css('a.next::attr(href)').get() # Селектор для ссылки на следующую страницу
        if next_page: # Если есть следующая страница
            yield scrapy.Request(response.urljoin(next_page), self.parse) # Переход на следующую страницу

#Запуск паука по команде в терминале: scrapy crawl lighting



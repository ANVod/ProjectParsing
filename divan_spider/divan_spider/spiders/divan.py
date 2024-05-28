import scrapy

class LeroyMerlinSpider(scrapy.Spider):
    name = "leroy_merlin"
    allowed_domains = ["leroymerlin.ru"]
    start_urls = [
        'https://leroymerlin.ru/catalogue/dreli-shurupoverty/'
    ]

    def parse(self, response):
        # Проверяем, что элементы товара имеют класс 'product-card'
        for product in response.css('div.phytpj4_plp'):
            yield {
                'name': product.css('a[data-qa-product-name]::text').get(),
                'price': product.css('span[data-qa-product-price]::text').get(),
                'link': response.urljoin(product.css('a[data-qa-product-link]::attr(href)').get()),
            }

        # Переход на следующую страницу, если она есть
        next_page = response.css('a[data-qa-pagination-next]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
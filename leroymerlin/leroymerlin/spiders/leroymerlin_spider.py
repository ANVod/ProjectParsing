import scrapy
from scrapy.http import Request


class LeroymerlinSpider(scrapy.Spider):
    name = "leroymerlin_spider"
    allowed_domains = ["leroymerlin.ru"]
    start_urls = [
        "https://leroymerlin.ru/catalogue/dreli-shurupoverty/"
    ]

    def parse(self, response):
        # Получаем ссылки на страницы с шуруповертами
        products = response.css('div.pr7cfcb_plp largeCard')

        for product in products:
            title = product.css('span.p1h8lbu4_plp sk-check-for-highlights.p::text').get()
            price = product.css('span.mncjxni_plp sk-check-for-highlights.span::text').get()
            link = product.css('a.t3y6ha_plp sn92g85_plp p16wqyak_plp::attr(href)').get()

            if title and price and link:
                yield {
                    'title': title.strip(),
                    'price': price.strip(),
                    'link': response.urljoin(link.strip())
                }

        # Переход на следующую страницу, если она существует
        next_page = response.css('a.next-paginator-button::attr(href)').get()
        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)

# Leroy Merlin. Scrapy. Web Scraping
import scrapy

class LeroymerlinMirrorsSpider(scrapy.Spider):
    name = "leroymerlin_mirrors"
    allowed_domains = ["leroymerlin.ru"]
    start_urls = ["https://leroymerlin.ru/catalogue/zerkala-v-vannuyu-komnatu/"]

    def parse(self, response):
        mirrors = response.css('div.pr7cfcb_plp largeCard')

        for mirror in mirrors:
            yield {
                'name': mirror.css('div.p1h8lbu4_plp span::text').get(),
                'price': mirror.css('div.mncjxni_plp span::text').get(),
                'url': mirror.css('a.bex6mjh_plp').attrib['href']
            }

        # Переход на следующую страницу, если она есть
        next_page = response.css('a[data-qa-pagination-item="right"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
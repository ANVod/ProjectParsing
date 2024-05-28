import scrapy


class DivanSpider(scrapy.Spider):
    name = "divan"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany"]

    def parse(self, response):
        for product in response.css("div.product-card"):
            yield {
                'name': product.css("a.product-card__name::text").get(),
                'price': product.css("div.product-card__price::text").get(),
                'link': response.urljoin(product.css("a.product-card__name::attr(href)").get()),
            }

        # Follow pagination links
        next_page = response.css("a.pagination__next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
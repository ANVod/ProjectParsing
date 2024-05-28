import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["leroymerlin.ru"]
    start_urls = ["https://leroymerlin.ru/catalogue/svet/"]

    def parse(self, response):
        for product in response.css("div.phytpj4_plp"):
            yield {
                'name': product.css("a.ui-product-card__name::text").get().strip(),
                'price': product.css("span.ui-product-card__price span.ui-product-card__price-value::text").get(),
                'link': response.urljoin(product.css("a.ui-product-card__name::attr(href)").get()),
            }

        # Follow pagination links
        next_page = response.css("a.paginator-button-next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

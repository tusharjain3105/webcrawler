import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon1"
    page=2
    def start_requests(self):
        url = 'https://www.amazon.in/s/i=fashion'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for items in response.css('h3'):
            url=items.css('a::attr(href)').get()
            yield {
                'scrapy.Request(response.urljoin(url), self.parse_items)':url
            }

    # def parse_cat(self, response):
    #     if Amazon_Fashion.availability==1:
    #         url=response.css('#p_n_availability-title+ .a-spacing-medium .a-spacing-micro a::attr(href)').get()
    #         yield scrapy.Request(response.urljoin(url), self.parse_cat)
    #         Amazon_Fashion.availability = 0
    #     elif Amazon_Fashion.product_page==0:
    #         url=response.css('.s-line-clamp-2 a::attr(href)')
    #         if url is not None:
    #             Amazon_Fashion.product_page = 1
    #             yield scrapy.Request(response.urljoin(url), self.parse_cat)
    #             next_page = response.request.url + "&page=" + str(Amazon_Fashion.page)
    #             if next_page is not None:
    #                 Amazon_Fashion.page += 1
    #                 yield response.follow(next_page, callback=self.parse)
    #     else:
    #         yield {
    #             'name': response.css('span.a-size-large::text').get().strip(),
    #             'price': response.css('#priceblock_ourprice::text').get(),
    #             'link': response.request.url,
    #             'description': response.css(
    #                 'div.a-section.a-spacing-medium.a-spacing-top-small span.a-list-item::text').getall(),
    #             'technical_details': response.css('.col1 td::text').getall(),
    #             'additional_details': response.css('.col2 td::text').getall(),
    #         }
    #
    #


import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    page=2
    def start_requests(self):
        url = 'https://www.amazon.in/s?k='
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag
        yield scrapy.Request(url, self.parse)



    def parse(self, response):
        for items in response.css('div.s-include-content-margin.s-border-bottom.s-latency-cf-section'):
            url=items.css('a.a-link-normal.a-text-normal::attr(href)').get()
            yield scrapy.Request(response.urljoin(url), self.parse_items)
            next_page=response.request.url+"&page="+str(AmazonSpider.page)
            if next_page is not None:
                AmazonSpider.page+=1
                yield response.follow(next_page, callback=self.parse)

    def parse_items(self, response):
        yield {
            'name': response.css('span.a-size-large::text').get().strip(),
            'price': response.css('#priceblock_ourprice::text').get(),
            'link': response.request.url,
            'description': response.css(
                'div.a-section.a-spacing-medium.a-spacing-top-small span.a-list-item::text').getall(),
            'technical_details': response.css('.col1 td::text').getall(),
            'additional_details': response.css('.col2 td::text').getall(),
        }




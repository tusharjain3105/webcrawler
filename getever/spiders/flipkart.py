import scrapy
class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    page= 2
    def start_requests(self):
        url = 'https://www.flipkart.com/search?q='
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for item in response.css('div._3liAhj, div._1UoZlX'):
            url = item.css('a._31qSD5::attr(href), a._2cLu-l::attr(href)').get()
            yield scrapy.Request(response.urljoin(url), self.parse_items)
            next_page=response.request.url+"&page="+str(FlipkartSpider.page)
            if next_page is not None:
                FlipkartSpider.page+=1
                yield response.follow(next_page, callback=self.parse)

    def parse_items(self, response):
        yield{
            'name': response.css('span._35KyD6::text').get().strip(),
            'price': response.css('div._1vC4OE._3qQ9m1::text').re_first(r'₹\s *(.*)'),
            'original_price': response.css('div._3auQ3N._1POkHg::text').re_first(r'₹\s *(.*)'),
            'discount': response.css('div.VGWI6T._1iCvwn span::text').get(),
            'rating': response.css('div._1i0wk8::text').get(),
            'url': response.request.url,
            'description': response.css('li._2-riNZ::text').getall(),
            'technical_details': response.css('._3YhLQA::text , .col.col-3-12::text').getall(),
        }
import scrapy
class FlipkartSpider(scrapy.Spider):
    name = 'flipkartall'
    page= 2
    def start_requests(self):
        url = 'https://www.flipkart.com'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        categories=[]
        for category in response.css('._3Lgyp8::text'):
            categories.append(category.get())
        print(categories)
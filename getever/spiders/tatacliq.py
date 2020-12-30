import scrapy
class tatacliq(scrapy.Spider):
    name='tatacliq'
    def start_requests(self):
        tag = getattr(self, 'tag', None)
        url="https://www.tatacliq.com/search/?searchCategory=all&text="+tag
        yield scrapy.Request(url, self.parse)
    def parse(self, response):
        for item in response.css('div._3u4ax-EVLYFqlQAtmD1PBM'):
            url=item.css('a::attr(href)')
            yield scrapy.Request(response.urljoin(url), self.parse_items)
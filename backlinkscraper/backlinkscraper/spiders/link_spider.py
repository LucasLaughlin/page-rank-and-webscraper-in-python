import scrapy
import numpy
from backlinkscraper.items import BacklinkscraperItem  

class LinkSpider(scrapy.Spider):
    name = "link_spider"
    start_urls = ['http://books.toscrape.com/']
    allowed_domains = ['books.toscrape.com']
    
    def parse(self, response):
        items = BacklinkscraperItem()
        
        items['url'] = response.request.url
        forward_links = []
        all_a_urls = response.css('a')
        for a in all_a_urls:
            url = a.css('a::attr(href)').extract_first()
            forward_links.append(response.urljoin(url))
        items['forward_links'] = forward_links
        yield items
        
        for x in forward_links:
            yield scrapy.Request(
                x,
                callback=self.parse
            )
    
    







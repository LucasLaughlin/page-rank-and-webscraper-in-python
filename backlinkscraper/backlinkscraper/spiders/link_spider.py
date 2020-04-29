import scrapy
import numpy
from backlinkscraper.items import BacklinkscraperItem


class LinkSpider(scrapy.Spider):
    name = "link_spider"
    allowed_domains = ['wikipedia.org']                         # Prevents crawler from scraping urls outside this domain
    start_urls = ['https://www.wikipedia.org']                  # Initial page scraped
    
    def parse(self, response):
        items = BacklinkscraperItem()
        
        items["url"] = response.request.url                     # save the url of the current page
        forward_links = []
        all_a_urls = response.css("a")
        for a in all_a_urls:                                    # iterate over all <a> tags containing links
            url = a.css("a::attr(href)").extract_first()        # save the href parameter of <a>, containing href
            forward_links.append(response.urljoin(url))
        items["forward_links"] = forward_links                  # save the list of foreward links from this page
        yield items                                             # pass the url and foreward links to the ouput
        
        for x in forward_links:                                 # Recursively call parse on links from current page
            yield scrapy.Request(x, callback=self.parse)
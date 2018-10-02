from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.loader import ItemLoader
from scrapy.linkextractor import LinkExtractor


class Articulos(Item):
    title = Field()
    description = Field()


class ComputrabajoSpider(CrawlSpider):

    name = "mi primer crowlspider"
    start_urls = ['https://www.ve.computrabajo.com/ofertas-de-trabajo/']
    allowed_domain = ['www.ve.computrabajo.com/']

    rules = (
    	    Rule(LinkExtractor(allow=r'p=')),
            Rule(LinkExtractor(allow=r'/oferta-de-trabajo-de-'), callback='parse_items'),
            )

    def parse_items(self, response):
        item = ItemLoader(Articulos(), response)     
        item.add_xpath('title', '//*[@id="MainContainer"]/article/section[1]/div[1]/div/h2/text()')
        item.add_xpath('description', '//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[3]/text()')
        yield item.load_item()

# scrapy runspider multiplepages.py -o ../../resources/computrabajo.csv -t csv
# pip install Scrapy

from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader


class Articulos(Item):
	title = Field()
	id = Field()


class PythonizaSpider(Spider):
    name = "mi primer spider"
    start_urls = ['https://www.pythoniza.me/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('/html/body/div[2]/div/div/div/div[1]/div[3]/div')

        for i, elem in enumerate(articulos):
            item = ItemLoader(Articulos(), elem)
            item.add_xpath('title', './/h3/text()')
            item.add_value('id', i)
            yield item.load_item()

# se ejecuta con el siguiente comando
# scrapy runspider onepage.py -o pythoniza.csv -t csv

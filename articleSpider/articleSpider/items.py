# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	articleName = scrapy.Field()
	articleWriter = scrapy.Field()
	articleTime = scrapy.Field()
	articleUrl = scrapy.Field()
class HabrItem(scrapy.Item):
	publisher= scrapy.Field()
	title = scrapy.Field()
	cuttext = scrapy.Field()
	link = scrapy.Field()

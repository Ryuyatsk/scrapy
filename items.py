# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PyjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    category = scrapy.Field() #カテゴリ
    name = scrapy.Field() #名前
    price = scrapy.Field() #価格
    image = scrapy.Field() #写真
    url = scrapy.Field() #URL
    # size = scrapy.Field() #サイズ
    description = scrapy.Field() #説明

   	


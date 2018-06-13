# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class blablacarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field()
    destination = scrapy.Field()
    departure_point = scrapy.Field()
    drop_off_point = scrapy.Field()
    departure_date= scrapy.Field()
    options= scrapy.Field()
    seats_left= scrapy.Field()
    car_owner_image= scrapy.Field()
    car_owner_name= scrapy.Field()
    car_owner_age= scrapy.Field()
    car_owner_verification= scrapy.Field()
    car_owner_rating = scrapy.Field()
    car_model= scrapy.Field()
    car_colour= scrapy.Field()
    pass

import scrapy
import string


class BlablacarSpider(scrapy.Spider):
	name = 'ride'
	allowed_domains = ['blablacar.in']
	base_url = 'https://blablacar.in'
	start_urls = ['https://blablacar.in/ride-sharing/' +char for char in string.ascii_lowercase]
	def parse(self, response):
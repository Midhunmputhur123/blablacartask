import scrapy
import string


class BlablacarSpider(scrapy.Spider):
	name = 'ride'
	allowed_domains = ['blablacar.in']
	base_url = 'https://blablacar.in'
	start_urls = ['https://blablacar.in/ride-sharing/' + char for char in string.ascii_lowercase]

	def parse(self, response):
		city_urls = response.xpath(
            '//div[@class="row"]//a[@class="u-blue"]/@href').extract()
		for url in city_urls:
            yield scrapy.Request(self.base_url + url, callback=self.city_details)

     def city_details(self, response):
     	ride_url = response.xpath(
            '//ul[@class="trip-search-results"]/li[@class="trip relative"]/a/@href'
        ).extract()
        for url in ride_url:
        	 yield scrapy.Request(self.base_url + url, callback=self.rider_details)



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

    def rider_details(self , response):
    	#xpath details

    	final_route = '//h1[@class="RideName RideName--title"]//span//text()'
    	dep_point = '//span[@data-position="departure"]/span/text()'
    	drop_point = '//span[@data-position="arrival"]/span/text()'
    	dep_date = '//strong[@class="RideDetails-infoValue"]//span/text()'
    	options = '//span[@class="u-alignMiddle"]/text()'
    	price = '//span[@class="Booking-price u-block"]/text()'
    	seats = '//span[@class="Booking-seats u-block"]/b/text()'
    	own_image = '//div[@class="ProfileCard"]//div[@class="ProfileCard-picture"]//img/@src'
    	own_name = '//div[@class="ProfileCard"]//div[@class="ProfileCard-infosBlock"]//h4//text()'
    	own_desc = '//div[@class="ProfileCard"]//div[@class="ProfileCard-infosBlock"]//div[@class="ProfileCard-info u-blue"]/text()'
    	rate = '//span[@class="u-textBold u-darkGray"]/text()'
    	own_age = '//div[@class="ProfileCard"]//div[@class="ProfileCard-infosBlock"]//div[@class="ProfileCard-info"]/text()'
    	car = '//div[@class="Profile-car u-table"]//p[@class="Profile-carDetails u-cell"]/text()'



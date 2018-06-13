import scrapy
import string
from dateparser import parse as parse_date
from blablacar.items import blablacarItem

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

    	#data extraction
    	route = response.xpath(final_route).extract()
    	dep_point = response.xpath(dep_point).extract()
    	drop_point = response.xpath(drop_point).extract()
    	dep_date = response.xpath(dep_date).extract()
    	options = response.xpath(options).extract()
    	price = response.xpath(price).extract()
    	seats = response.xpath(seats).extract()
    	image = response.xpath(own_image).extract()
    	name = response.xpath(own_name).extract()
    	age = response.xpath(own_age).extract()
    	description = response.xpath(own_desc).extract()
    	rating = response.xpath(rate).extract()
    	car = response.xpath(car).extract()

    	#cleaning of data
    	departure = ''.join(dep_point).strip()
    	droping =''.join(drop_point).strip()
    	date =''.join(dep_date).strip()
    	options =''.join(options).strip()
    	price =''.join(price).strip().replace('₹\xa0', '')
    	seats =''.join(seats).strip()
    	image =''.join(image).strip()
    	name =''.join(name).strip()
    	age =''.join(age).strip().replace(' years old', '')
    	description =''.join(description).strip()
    	rating =''.join(rating).strip()


    	if route:
    		source = route[0]
    		destination = route[-1]

    	if car :
    		car_model1 = car[0]
    		car_color = car[1].strip()

    	yield  blablacarItem(
    		source=source,
    		destination=destination,
    		departure_point=departure,
    		drop_off_point=droping,
    		departure_date=date,
    		options=options,
    		seats_left=seats,
    		car_owner_image=image,
    		car_owner_name=name,
    		car_owner_age=age,
    		car_owner_verification=description,
    		car_owner_rating = rating,
    		car_model=car_model1,
    		car_colour=car_color
    		)





# -*- coding: utf-8 -*-
import scrapy
from typing import List
from CarDataScrape1.CarDataScrape.items import CarDataItemLoader
from CarDataScrape1.CarDataScrape.items import CarDataItem
import itertools


class MsrpSpider(scrapy.Spider):
    name = 'MsrpSpider'
    allowed_domains = ['https://www.jdpower.com']

    def start_requests(self):
        makes: List[str] = ['Acura', 'Aston-Martin', 'Audi', 'BMW', 'Buick', 'Cadillac',
                            'Chevrolet', 'Chrysler', 'Dodge', 'FIAT', 'Ford', 'GMC', 'Honda',
                            'Hummer', 'Hyundai', 'INFINITI', 'Jaguar', 'Jeep', 'Kia',
                            'Land-Rover', 'Lexus', 'Lincoln', 'Lotus', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan',
                            'Oldsmobile', 'Panoz', 'Plymouth', 'Pontiac', 'Porsche',
                            'Ram-Truck', 'Scion', 'Subaru',
                            'Tesla-Motors', 'Toyota',
                            'Volkswagen', 'Volvo']

        def makes_urls(makes):
            urls = []
            urls.append([f"https://www.jdpower.com/Cars/2019/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2018/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2017/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2016/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2015/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2014/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2013/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2012/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2011/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2010/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2009/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2008/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2007/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2006/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2005/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2004/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2003/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2002/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2001/{make}" for make in makes])
            urls.append([f"https://www.jdpower.com/Cars/2000/{make}" for make in makes])

            urls = list(itertools.chain.from_iterable(urls))
            # urls = [y for x in urls for y in x]

            return urls

        urls = makes_urls(makes)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for vehicle in response.css('div.veh-spacer'):
            yield {
            }

from typing import List
import itertools
import pprint as pp

makes: List[str] = ['Acura', 'Alfa-Romeo', 'Aston-Martin', 'Audi', 'Bentley', 'BMW', 'Buick', 'Cadillac',
                    'Chevrolet', 'Chrysler',
                    'Daewoo', 'Dodge', 'Ferrari', 'FIAT', 'Fisker', 'Ford', 'Freightliner-Light-Duty',
                    'Genesis', 'GMC', 'Honda',
                    'Hummer', 'Hyundai', 'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Karma-Automotive', 'Kia',
                    'Lamborghini',
                    'Land-Rover', 'Lexus', 'Lincoln', 'Lotus', 'Maserati', 'Maybach', 'Mazda', 'McLaren',
                    'Mercedes-Benz',
                    'Mercury', 'MINI', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Panoz', 'Plymouth', 'Pontiac',
                    'Porsche',
                    'Ram-Truck', 'Rolls-Royce', 'Saab', 'Saturn', 'Scion', 'smart', 'Subaru', 'Suzuki',
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
    urls = list(itertools.chain.from_iterable(urls))
    # urls = [y for x in urls for y in x]

    return urls


urls = makes_urls(makes)


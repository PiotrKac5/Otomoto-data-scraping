import requests
from bs4 import BeautifulSoup
import csv


class Car:
    brand: str
    model: str
    year: int
    mileage: str
    engine_capacity: str
    fuel_type: str
    price: int


class scraper:
    def __init__(self, filters): # filters is a dict of filters by properties of car class
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.11 (KHTML, like Gecko) "
            "Chrome/23.0.1271.64 Safari/537.11",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
        }

        self.filters = filters
        self.website = "https://www.otomoto.pl/osobowe"

    def scrape_pages(self):
        cars = []
        number_of_pages = 0


    def get_website(self):
        first = True
        if 'brand' in self.filters.keys():
            self.website += f"/{self.filters['brand']}"
        if 'model' in self.filters.keys():
            self.website += f"/{self.filters['model']}"
        if 'year' in self.filters.keys():
            if first:
                first = False
            self.website += f"/od-{self.filters['year'][0]}?search%5Bfilter_float_year%3Ato%5D={self.filters['year'][1]}"
        if 'mileage' in self.filters.keys():
            if first:
                self.website += "?"
                first = False
            else:
                self.website += "&"
            self.website += f"search%5Bfilter_float_mileage%3Afrom%5D={self.filters['mileage'][0]}&search%5Bfilter_float_mileage%3Ato%5D={self.filters['mileage'][1]}"
        if 'engine_capacity' in self.filters.keys():
            if first:
                self.website += "?"
                first = False
            else:
                self.website += "&"
            self.website += f"search%5Bfilter_float_engine_capacity%3Afrom%5D={self.filters['engine_capacity'][0]}&search%5Bfilter_float_engine_capacity%3Ato%5D={self.filters['engine_capacity'][1]}"
        if 'fuel_type' in self.filters.keys():
            if first:
                self.website += "?"
                first = False
            else:
                self.website += "&"
            self.website += f"search%5Bfilter_enum_fuel_type%5D={self.filters['fuel_type']}"
        if 'price' in self.filters.keys():
            if first:
                self.website += "?"
                first = False
            else:
                self.website += "&"
            self.website += f"search%5Bfilter_float_price%3Afrom%5D={self.filters['price'][0]}&search%5Bfilter_float_price%3Ato%5D={self.filters['price'][1]}"




# F = {'brand': 'Ford', 'model':'focus', 'year': [2007, 2015], 'fuel_type':'petrol', 'price':[10000, 20000], 'mileage':[100000, 200000], 'engine_capacity':[1250, 1500]}
# x = scraper(F)
# x.get_website()


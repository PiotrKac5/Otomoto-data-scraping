import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict
import csv

@dataclass
class Car:
    link: str
    # full_name: str
    # brand: str
    # model: str
    year: str
    mileage: str
    engine_capacity: str
    fuel_type: str
    price: str


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

    def scrape_pages(self, number_of_pages):
        self.get_website()
        cars = []
        for i in range(1, number_of_pages+1):
            curr_website = self.website + f"&page={i}"
            new_cars = self.get_cars_from_current_page(curr_website)
            if new_cars:
                cars += (new_cars)
        return cars

    def get_cars_from_current_page(self, curr_website):
        try:
            response = requests.get(curr_website, headers=self.headers).text
            soup = BeautifulSoup(response, "html.parser")
            cars = self.extract_cars(soup)
            return cars
        except Exception as e:
            print(f"Problem with website: {curr_website}, reason: {e}")
            return []


    def extract_cars(self, soup):
        offers = soup.find("div", class_="ooa-r53y0q esqdut111")
        cars = offers.find_all("article")
        cars_list = []
        for car in cars:
            try:
                link = car.find("h1", class_="e1vic7eh9 ooa-1ed90th er34gjf0").find("a", href=True).get("href")

                engine_capacity = car.find("p", class_="e1vic7eh10 ooa-1tku07r er34gjf0").text.strip()[:9]

                year = (car.find("dd", class_="ooa-1omlbtp e1vic7eh13", attrs={"data-parameter":"year"}).text.strip())

                fuel_type = car.find("dd", class_="ooa-1omlbtp e1vic7eh13", attrs={"data-parameter": "fuel_type"}).text.strip()

                mileage = car.find("dd", class_="ooa-1omlbtp e1vic7eh13", attrs={"data-parameter": "mileage"}).text.strip()

                price = (car.find("h3", class_="e1vic7eh16 ooa-1n2paoq er34gjf0").text.strip())

                cars_list.append(
                    Car(
                        link=link,
                        year=year,
                        mileage=mileage,
                        engine_capacity=engine_capacity,
                        fuel_type=fuel_type,
                        price=price,
                    )
                )


            except Exception as e:
                print(f"Error msg: {e}")
        return cars_list

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


def write_to_csv(cars):
    with open("cars.csv", mode="w") as f:
        fieldnames = [
            "link",
            # "full_name",
            "year",
            "mileage",
            "engine_capacity",
            "fuel_type",
            "price",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for car in cars:
            writer.writerow(asdict(car))


if __name__ == "__main__":
    # F = {'brand': 'Ford', 'model': 'focus', 'year': [2007, 2015], 'fuel_type': 'petrol', 'price': [10000, 20000],
    #      'mileage': [100000, 200000], 'engine_capacity': [1250, 1500]}
    F = {'brand': 'Ford', 'model': 'focus', 'year': [2000, 2020]}
    x = scraper(F)
    # x.get_website()

    # print(x.scrape_pages(1))
    write_to_csv(x.scrape_pages(108))





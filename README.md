# Otomoto scraping tool
Web scraping program written in python using BeautifulSoup library to parse HTML data. After successful parsing program is writting all information to a csv file *cars.csv*. In this file you will find links to actuall offers at *otomoto.pl* and in addition year, mileage(km), engine_capacity(${cm}^{3}$), fuel type and price(PLN) of each car. <br>
What is more, in file *graphing.py.ipynb* you can find some plots representing how different parameters of car affect price of it. 
<br>

## Why would you use it?
Application is useful when you want to check price of specific car brand and model, cars that were produced in specific time frame or in general get to know some statistics about car price at the polish market.
You could also explore different charts of how price is changing according to year or mileage of a car.

## How to use it?
At first open *getdata.py* file and run it, then put in your criteria, add how many pages of offers you want to scrape and wait for the data to be written in *cars.csv* file.
<br> <br>

*Warning! Somme error messages may occur because it is impossible to perfectly scrape all offers each time, so unfortunately some will be missed. If the only thing that program shows is "Problem with website: ... " Then run application again.* <br> <br>

Your next step is going to be open *graphin.py.ipynb* file and select run all. Then you will be able to see plots regarding price of cars according to different criteria.

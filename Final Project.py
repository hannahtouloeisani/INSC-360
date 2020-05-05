# Importing needed libraries
import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(
    filename='final_project_logging',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

URL = "https://en.wikipedia.org/wiki/List_of_African_countries_by_population" # Specifiy which URL/web page we are going to be scrapping
res = requests.get(URL).text # Open the URl using requests
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]: # Exception handling
    data = items.find_all(['th','td']) # Use 'find_all' function to bring back all instances
    try: # Looks up information in each specified data row
        country = data[1].a.text
        offical_figure = data[2].text
        date_of_last_figure = data[3].text
        source = data[4].text
    except IndexError:pass
    print("{}: {} | {}: {} | {}: {}".format("Country",country,"Population",offical_figure,"Date of last figure",date_of_last_figure)) # Formatting my intended output
    logging.info("Country: " + country + "|Population: " + offical_figure) # Implements logging
    logging.info("Source of Information " + source)

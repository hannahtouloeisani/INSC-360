import requests
import logging
import datetime
from xml.etree import ElementTree as ET

logging.basicConfig(
    filename='hw8-logging',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)


with open ('hw8-text', 'r') as f:
    hw8 = f.readlines()
    for url in hw8:
        url = url.strip()
        r = requests.get(url)
        if r.status_code == 200:
            print("Attempting to retrieve data from:", r.url)
            print("200 - Successfully retrieved:", r.url)
            logging.info("Attempting to retrieve data from:" + r.url)
            logging.info("200 - Successfully retrieved:" + r.url)
            root = ET.fromstring(r.text)
            for customer in root.findall("customer"):
                id = customer.find('id').text
                name = customer.find('name').text
                checking_accounts = customer.findall('checking_account')
                savings_account = customer.findall('savings_account')
                for account in checking_accounts:
                    print(name, "Checking Account:", account.text)
                    logging.info("Now processing Customer ID " + str(id))
                for accounts in savings_account:
                    print(name, "Savings Account:", accounts.text)
                    logging.info("Now processing Customer ID " + str(id))
        elif r.status_code == 404:
            print("Attempting to retrieve data from:", r.url)
            print("Resource not found")
            logging.error("Attempting to retrieve data from:" + r.url)
            logging.error("404 - Resource not found")


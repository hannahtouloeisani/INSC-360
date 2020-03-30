
#  Auth: Hannah Touloeisani
#  Date: March 9, 2020
#  File: Homework-5

import csv
import logging
import datetime

logging.basicConfig(
    filename='log-hw5' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

counter = 0
with open ('input-data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  next(reader)  # Python next() skips to the next line. So skipping the header row
  for row in reader:
    counter += 1
    try:
        sales_total = int(row[1]) + int(row[2]) + int(row[3])
        print("{} - Total first quarter sales for store {}: ${:,}".format(counter, row[0], sales_total))
        logging.info('Successfully opened and read input file. Processed record number' + str(counter))
    except Exception as e:
        print(e)
        print("Data missing in row")
        logging.error("Error processing record")




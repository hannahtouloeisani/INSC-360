
#  Auth: Hannah Touloeisani
#  Date: March 9, 2020
#  File: Homework-5

import csv

counter = 0
with open ('input-data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  next(reader)  # Python next() skips to the next line. So skipping the header row
  for row in reader:
    counter += 1  # keep track of how many records we have processed.
    sales_total = int(row[1]) + int(row[2]) + int(row[3])
    print("{} - Total first quarter sales for store {}: ${:,}".format(counter, row[0], sales_total))

try:
    row[1] = int(row[1])
    row[2] = int(row[2])
    row[3] = int(row[3])
    row[4] = int(row[4])
    row[5] = int(row[5])
    row[6] = int(row[6])
except ValueError: # process ValueError only
  print("Invalid data, row is skipped")


import logging
import datetime

logging.basicConfig(
    filename='log-hw5' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.ERROR)
logging.info('Successfully opened and read input file.', 'Processed record number')
logging.error("Error processing record")



# Author: Hannah Touloeisani
# Date: 2/9/20
#Description: Assignment 3

from datetime import date
today = date.today()  #(2)
print(today)
today_date_string = today.strftime("%m/%d/%Y") #(3)
print(today_date_string)
from datetime import datetime
graduation_string = "May 15, 2020"  #(4)
datetime_obj_1 = datetime.strptime(graduation_string, "%B %d, %Y") #(5)
print(datetime_obj_1)

month = datetime_obj_1.month  #(6)
day = datetime_obj_1.day
year = datetime_obj_1.year

print(month)
print(day)
print(year)

import calendar

today_weekday = today.weekday()  #(7)
print(today_weekday)
print("Better known as: " + str(calendar.day_name[today_weekday]))
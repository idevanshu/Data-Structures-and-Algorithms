from datetime import datetime

def dayOfYear(date):
    year, month, day= (int(i) for i in date.split("-"))
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] += 1
    
    day_of_year = sum(days_in_month[:month-1]) + day
    return day_of_year 

print(dayOfYear("2019-03-1"))
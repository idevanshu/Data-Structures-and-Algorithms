from datetime import datetime

def dayOfTheWeek(year,month,day): 
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dt = datetime(year, month, day)
        return weekdays[dt.weekday()]

print(dayOfTheWeek(day = 18, month = 7, year = 1999))


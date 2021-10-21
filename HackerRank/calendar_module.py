import calendar
import datetime

n = raw_input()
month, day, year = (int(x) for x in n.split(' '))

def findDay(date):
    theDay = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[theDay].upper())
 
# Driver program
date = n
if year > 2000 and year < 3000: 
    print(findDay(date))

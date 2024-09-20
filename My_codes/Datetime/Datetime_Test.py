from datetime import date, time, datetime
from dateutil import parser
import dateparser

print()
print(date(year=2021, month=10, day=22))
print()
print(time(hour=10, minute=19, second=10))
print()
print(datetime(year=2021, month=10, day=22, hour=10,  minute=19, second=10))
print(datetime.now())
print(datetime.today())
print(date.today())
print()
now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)
print()
today = date.today()
print(today)
tomorrow = today.replace(day=today.day + 1) # ! cette methode ne prends pas en compte les fuseaux horaire tec...
print(tomorrow)
print()
# print(date.isoformat("2021-10-24"))
# print(date.strptime("22 Oct 2024", ""))
print(datetime.strptime("22 Oct 2024", "%d %b %Y")) # https://strftime.org/
now = datetime.now()
print(now.strftime("%d %B %Y")) # https://strftime.org/
print()
print(parser.parse("24 October 2024 at 9am and 18 minutes"))
print()
print(dateparser.parse("aujourd'hui"))
print(dateparser.parse("demain"))
print(dateparser.parse("ontem"))   # (portugais) 
print()


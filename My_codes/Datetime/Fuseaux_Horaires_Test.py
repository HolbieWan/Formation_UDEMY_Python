# tz database (fuseaux horaires officiels)
# UTC= Temps Universel Coordoné.  (echelle de temps universelle, tous les fuseaux horaires se réferrent à l'UTC)
# UTC DST = Day Saving Time (Heure été)
# EDT = Eastern Daylight Time
# EST = Eastern Standard Time
# PDT = Pacific Daylight Time
# PST = Pacific Standard Time
# date naive (ne prend pas en compte les fuseaux horaires)
# date aware (prend en compte les fuseaux horaires)

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

now = datetime.now()
print(now.tzinfo)

now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
print(now_in_vancouver)

now_in_montreal = datetime.now(tz=ZoneInfo("America/Montreal"))
print(now_in_montreal)
print()

now_in_paris = datetime.now()
now_in_paris.tzinfo

# now_in_montreal > now_in_paris   # can't compare naive with aware... -> error

now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))
print(now_in_paris)
print()

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))
march_8 = march_7_utc + timedelta(days=1)
march_8 = march_8.astimezone(montreal_tz)
print(march_7)
print(march_8)
print()

march_10 = datetime(2020, 3, 10, 13, 0, 0, tzinfo=montreal_tz)
march_10_utc = march_10.astimezone(ZoneInfo("UTC"))
print(march_10_utc)
print(march_10 - march_7)
print(march_10_utc - march_7_utc)
print()

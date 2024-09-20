from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
now_in_15_days_minus_5_hours = now + timedelta(days=15, hours=-5)
print(now)
print(now_in_15_days_minus_5_hours)

feb_27_2022 = datetime(2022, 2, 27)
print(feb_27_2022 + timedelta(days=3))
print()

now = datetime.now()
now_in_2_months = now + relativedelta(months=2)
print(now)
print(now_in_2_months)

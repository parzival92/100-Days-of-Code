import datetime as dt

now = dt.datetime.now()
# Print Year
print(now.year)
# Print Month
print(now.month)
# Date
print(now.date())
# Weekday
print(now.weekday())

date_of_birth = dt.datetime(year=1992,month=8,day=10)
print(date_of_birth)
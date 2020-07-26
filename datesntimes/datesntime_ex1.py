# let's first look at dates.

import datetime

# difference between naive and aware times.

# Naive Dates --> Don't have enough information to determine daylight savings or timezones but are easier to work with
# Aware Dates and Times --> Have information missing in Naive Dates.

d = datetime.date(2016, 7, 24)                  # No leading zeros!
print(d)

tday = datetime.date.today()
print(tday)
# Want to grab just the year?
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

# weekday --> Monday = 0 and Sunday = 7
# isoweekday --> Monday = 1 and Sunday = 7

# let's let at time deltas.

tdelta = datetime.timedelta(days=7)     # this is an object that can be added and subtracted from a date to get a new date.
                                        # A time delta can be acquired by adding or subtracting a date to/from any other date.

# let's print what the date will be one week from now.

print(tday + tdelta)                    # this will only give a new date.

bday = datetime.date(2021, 6, 8)

till_bday = bday - tday                 # this will give us a timedelta.
print(till_bday.total_seconds())
# let's work now with time.

import datetime

t = datetime.time(9, 30, 45, 100000)
print(t.hour)

# but what if only time or only date doesn't fulfill our purpose?
# We can use datetime.datetime.

dt = datetime.datetime(2020, 9, 30, 12, 30, 45, 100)

print(dt.year)

# can also acquire deltas in datetime as well.

tdelta = datetime.timedelta(hours = 12)

print(dt + tdelta)
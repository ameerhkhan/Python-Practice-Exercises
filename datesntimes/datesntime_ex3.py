import datetime
import pytz

dt_today = datetime.datetime.today()    # returns current local datetime with a timezone of now.
dt_now = datetime.datetime.now()        # allows passage of an argument that may define a timezone.
dt_utcnow = datetime.datetime.utcnow()  # Is this a timezone aware function? NO!

# We have to explicitly set timezones.

# pip install pytz for working with timezones.

# Even Python official documentation recommends usage of pytz.

# pytz is recommended to always work with UTC when working with timezones.

# let's create a timezone aware time using UTC.

dt = datetime.datetime(2020, 1, 9, 12, 39, 45, tzinfo=pytz.UTC)
# print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# let's convert the time into some other timezone.
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain')) # for Karachi use, Asia/Karachi.
print(dt_mtn)

dt_khi = dt_utcnow.astimezone(pytz.timezone('Asia/Karachi'))
print(dt_khi)

# let's print out all the timezones.

# for tz in pytz.all_timezones:
#     print(tz)

# let's now get a naive datetime.

dt_na = datetime.datetime.now()

# Now how to convert this naive datetime?
mtn_khi = pytz.timezone('Asia/Karachi')
# now converting using localize
dt_kh = mtn_khi.localize(dt_na)
print(dt_kh)

dt_east = dt_kh.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
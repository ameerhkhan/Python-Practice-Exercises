# Let's look at ways we can diplay these datetimes.

import datetime
import pytz


dt_khi = datetime.datetime.now(tz=pytz.timezone('Asia/Karachi'))

print(dt_khi.isoformat())

# goto python documentation to find out about formats that you can use. Such as,
print(dt_khi.strftime('%B %d, %Y')) # will print July 22, 2020, which is one of the format that can be used to display the dates.
                                    # Basically converts any datetime into a string.


# sometimes we have a string and we want to convert it into a datetime.

dt_str = 'July 20, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
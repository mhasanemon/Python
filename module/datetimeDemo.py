import pytz
import datetime

country = 'Asia/Dhaka'
tz_to_display = pytz.timezone(country)
localtime = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country,localtime))
print("UTC is {}".format(datetime.datetime.utcnow()))